#!/usr/bin/env python3
"""
Reorganize Blog Posts for Weekly Sunday Publishing

This script:
1. Maps all posts to their week numbers using JSON content files
2. Redates all posts starting from Dec 14, 2025 (week 1)
3. Week 2+ scheduled for every Sunday after
4. Moves week 1 to _posts/, weeks 2-52 to drafts/
"""

import json
import os
import re
import shutil
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
START_DATE = datetime(2025, 12, 14)  # Week 1 publish date (today)
FIRST_SUNDAY = datetime(2025, 12, 21)  # First Sunday after start

def get_week_schedule():
    """Generate publish dates for all 52 weeks"""
    schedule = {}
    schedule[1] = START_DATE  # Week 1 is today (Saturday)

    for week in range(2, 53):
        # Weeks 2-52 are every Sunday
        days_after_first_sunday = (week - 2) * 7
        schedule[week] = FIRST_SUNDAY + timedelta(days=days_after_first_sunday)

    return schedule

def slugify(title):
    """Convert title to URL slug"""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug[:50].rstrip('-')

def load_week_titles():
    """Load title for each week from JSON files"""
    titles = {}
    for week in range(1, 53):
        json_path = Path(f'content/week-json/week-{week:02d}-content.json')
        if json_path.exists():
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                titles[week] = data.get('title', '')
    return titles

def find_post_by_title(title, search_dirs):
    """Find a post file that matches the given title"""
    title_slug = slugify(title)[:30]  # First 30 chars of slug

    for dir_path in search_dirs:
        if not Path(dir_path).exists():
            continue
        for file in Path(dir_path).glob('*.md'):
            # Check filename
            if title_slug in file.stem.lower():
                return file

            # Check front matter title
            try:
                content = file.read_text(encoding='utf-8')
                if f'title: "{title}"' in content or f"title: '{title}'" in content:
                    return file
                # Partial match
                if title[:40] in content:
                    return file
            except:
                pass

    return None

def update_post_frontmatter(file_path, new_date, week_num):
    """Update the date in post front matter"""
    content = file_path.read_text(encoding='utf-8')

    # Update date line
    date_str = new_date.strftime('%Y-%m-%d')
    content = re.sub(
        r'^date:\s*\d{4}-\d{2}-\d{2}.*$',
        f'date: {date_str} 08:00:00 -0500',
        content,
        flags=re.MULTILINE
    )

    file_path.write_text(content, encoding='utf-8')
    return date_str

def main():
    print("=" * 60)
    print("Reorganize Posts for Weekly Sunday Publishing")
    print("=" * 60)
    print()

    # Ensure we're in repo root
    if not Path('content/week-json').exists():
        print("ERROR: Run from repo root")
        return

    # Create drafts directory if needed
    Path('drafts').mkdir(exist_ok=True)

    # Get schedule
    schedule = get_week_schedule()
    print(f"Week 1: {schedule[1].strftime('%Y-%m-%d')} (Today)")
    print(f"Week 2: {schedule[2].strftime('%Y-%m-%d')} (Sunday)")
    print(f"Week 52: {schedule[52].strftime('%Y-%m-%d')}")
    print()

    # Load week titles
    titles = load_week_titles()
    print(f"Loaded {len(titles)} week titles from JSON")
    print()

    # Track results
    processed = 0
    week1_file = None

    # Process each week
    for week in range(1, 53):
        title = titles.get(week, '')
        if not title:
            print(f"[SKIP] Week {week:2d}: No title in JSON")
            continue

        # Find the post
        post_file = find_post_by_title(title, ['_posts', 'drafts'])

        if not post_file:
            print(f"[MISS] Week {week:2d}: {title[:40]}...")
            continue

        # Get new date
        new_date = schedule[week]
        date_str = new_date.strftime('%Y-%m-%d')

        # Update front matter
        update_post_frontmatter(post_file, new_date, week)

        # Determine destination
        slug = slugify(title)
        new_filename = f"week{week:02d}-{slug}.md"

        if week == 1:
            # Week 1 stays in _posts with date prefix
            dest_dir = Path('_posts')
            new_filename = f"{date_str}-{slug}.md"
            week1_file = dest_dir / new_filename
        else:
            # Weeks 2-52 go to drafts
            dest_dir = Path('drafts')

        dest_path = dest_dir / new_filename

        # Move file
        if post_file != dest_path:
            shutil.move(str(post_file), str(dest_path))

        print(f"[OK] Week {week:2d}: {dest_path.name}")
        processed += 1

    # Clean up: remove any leftover posts from _posts (except week 1)
    if week1_file:
        for file in Path('_posts').glob('*.md'):
            if file != week1_file:
                # Move to drafts or delete if duplicate
                print(f"[MOVE] Extra file: {file.name} -> drafts/")
                dest = Path('drafts') / file.name
                if not dest.exists():
                    shutil.move(str(file), str(dest))
                else:
                    file.unlink()

    print()
    print("=" * 60)
    print(f"Processed: {processed} posts")
    print(f"Week 1 in _posts/: {week1_file.name if week1_file else 'NOT FOUND'}")
    print(f"Drafts ready: {len(list(Path('drafts').glob('week*.md')))}")
    print("=" * 60)
    print()
    print("Next: git add . && git commit && git push")

if __name__ == '__main__':
    main()
