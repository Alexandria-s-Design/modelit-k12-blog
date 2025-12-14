#!/usr/bin/env python3
"""
Batch Generate Blog Posts from Week JSON Files

Converts weeks 15-52 from JSON content to Jekyll markdown posts.
Run from repo root: python scripts/batch_generate_posts.py
"""

import json
import os
import re
import shutil
from pathlib import Path

def slugify(title: str) -> str:
    """Convert title to URL-friendly slug"""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug[:50].rstrip('-')

def convert_week_to_post(week_num: int, dry_run: bool = False) -> str:
    """Convert a single week JSON to markdown post"""

    # Load JSON
    json_path = Path(f'content/week-json/week-{week_num:02d}-content.json')
    if not json_path.exists():
        raise FileNotFoundError(f"Missing: {json_path}")

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Parse date - handle various formats
    date_raw = data.get('publish_date', '')
    if date_raw:
        # Extract YYYY-MM-DD
        date_str = date_raw[:10]
        # Fix invalid dates like "2025-15-01"
        parts = date_str.split('-')
        if len(parts) == 3:
            year, month, day = parts
            # If month > 12, assume it's week number used as month - calculate real date
            if int(month) > 12:
                # Approximate: week N → early month ceil(N/4)
                real_month = min(12, max(1, (week_num - 1) // 4 + 1))
                day_offset = ((week_num - 1) % 4) * 7 + 1
                date_str = f"{year}-{real_month:02d}-{min(28, day_offset):02d}"
    else:
        # Default: calculate from week number (starting Nov 2025)
        # Week 1 = Nov 1, 2025
        base_week = 1
        base_month = 11
        base_year = 2025
        weeks_from_base = week_num - base_week
        month = base_month + (weeks_from_base // 4)
        year = base_year + (month - 1) // 12
        month = ((month - 1) % 12) + 1
        day = min(28, (weeks_from_base % 4) * 7 + 1)
        date_str = f"{year}-{month:02d}-{day:02d}"

    # Generate slug
    title = data.get('title', f'Week {week_num}')
    slug = slugify(title)

    # Get content sections
    content = data.get('content', {})

    # Build markdown
    md_lines = [
        '---',
        'layout: post',
        f'title: "{title}"',
        f'date: {date_str} 08:00:00 -0500',
        f'category: "{data.get("category", "Platform Spotlight")}"',
        f'author: "{data.get("author", "Dr. Marie & Charles Martin")}"',
        f'hero_image: "/assets/images/week{week_num}-hero.jpg"',
        f'excerpt: "{data.get("excerpt", "")}"',
        '---',
        '',
        content.get('opening_hook', ''),
        '',
        '---',
        '',
        f'## {content.get("section_1_title", "Section 1")}',
        '',
        content.get('section_1_text', ''),
        '',
        '---',
        '',
        f'## {content.get("section_2_title", "Section 2")}',
        '',
        content.get('section_2_text', ''),
        '',
        '---',
        '',
        f'## {content.get("section_3_title", "Section 3")}',
        '',
        content.get('section_3_text', ''),
        '',
        '---',
        '',
        f'## {content.get("section_4_title", "Section 4")}',
        '',
        content.get('section_4_text', ''),
        '',
        '---',
        '',
        '## Your Next Step',
        '',
        content.get('closing', ''),
        ''
    ]

    md_content = '\n'.join(md_lines)

    # Output path
    output_path = Path(f'_posts/{date_str}-{slug}.md')

    if not dry_run:
        # Write post
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        # Copy hero image
        src_img = Path(f'assets/hero-images/week-{week_num:02d}-hero.jpg')
        dst_img = Path(f'assets/images/week{week_num}-hero.jpg')

        if src_img.exists() and not dst_img.exists():
            dst_img.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(src_img, dst_img)

    return str(output_path)

def main():
    """Generate all remaining posts (weeks 15-52)"""
    print("=" * 60)
    print("ModelIt K-12 Blog Post Generator")
    print("=" * 60)
    print()

    # Ensure we're in repo root
    if not Path('content/week-json').exists():
        print("ERROR: Run from repo root (where content/week-json exists)")
        return

    # Ensure output dirs exist
    Path('_posts').mkdir(exist_ok=True)
    Path('assets/images').mkdir(parents=True, exist_ok=True)

    success = 0
    failed = 0

    for week in range(15, 53):
        try:
            output = convert_week_to_post(week)
            print(f"✓ Week {week:2d}: {output}")
            success += 1
        except Exception as e:
            print(f"✗ Week {week:2d}: {e}")
            failed += 1

    print()
    print("=" * 60)
    print(f"Complete: {success} generated, {failed} failed")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Review generated posts in _posts/")
    print("  2. git add _posts/ assets/images/")
    print("  3. git commit -m 'Add weeks 15-52 blog posts'")
    print("  4. git push origin master")

if __name__ == '__main__':
    main()
