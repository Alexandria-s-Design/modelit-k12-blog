# Gemini Batch Generation Plan: Complete 38 Remaining Blog Posts

## Summary
Convert weeks 15-52 from JSON content files to Jekyll markdown posts. The content already exists - this is a formatting/conversion task.

## Current Status
- **Written**: Weeks 1-14 (in `docs/blog-posts/` and `_posts/`)
- **Remaining**: Weeks 15-52 (38 posts)
- **Source**: `content/week-json/week-{15-52}-content.json`
- **Target**: `_posts/YYYY-MM-DD-{slug}.md`

## JSON Structure (Input)
Each `week-XX-content.json` contains:
```json
{
  "week_number": 15,
  "publish_date": "2025-01-15T08:00:00Z",
  "title": "...",
  "category": "...",
  "author": "Dr. Marie & Charles Martin",
  "excerpt": "...",
  "content": {
    "opening_hook": "...",
    "section_1_title": "...",
    "section_1_text": "...",
    "section_2_title": "...",
    "section_2_text": "...",
    "section_3_title": "...",
    "section_3_text": "...",
    "section_4_title": "...",
    "section_4_text": "...",
    "closing": "..."
  },
  "metadata": {
    "hero_image_filename": "week-15-hero.jpg"
  }
}
```

## Markdown Output Format
```markdown
---
layout: post
title: "{title}"
date: {publish_date formatted as YYYY-MM-DD HH:MM:SS -0500}
category: "{category}"
author: "{author}"
hero_image: "/assets/images/week{N}-hero.jpg"
excerpt: "{excerpt}"
---

{opening_hook}

---

## {section_1_title}

{section_1_text}

---

## {section_2_title}

{section_2_text}

---

## {section_3_title}

{section_3_text}

---

## {section_4_title}

{section_4_text}

---

## Your Next Step

{closing}
```

## File Naming Convention
- Input: `content/week-json/week-15-content.json`
- Output: `_posts/2025-01-15-teachers-pay-teachers-success.md`
- Slug: lowercase title, spaces → hyphens, remove special chars

## Image Handling
1. Hero images exist in `assets/hero-images/week-{NN}-hero.jpg` (with dash, zero-padded)
2. Copy to `assets/images/week{N}-hero.jpg` (no dash, no zero-pad) for consistency
3. Front matter uses: `hero_image: "/assets/images/week{N}-hero.jpg"`

## Batch Script (Python)
```python
import json
import os
from datetime import datetime
import re

def slugify(title):
    """Convert title to URL slug"""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    return slug[:50]  # Truncate for reasonable length

def convert_week_to_post(week_num):
    # Load JSON
    json_path = f'content/week-json/week-{week_num:02d}-content.json'
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Parse date
    date_str = data['publish_date'][:10]  # YYYY-MM-DD

    # Generate slug
    slug = slugify(data['title'])

    # Build markdown
    md = f"""---
layout: post
title: "{data['title']}"
date: {date_str} 08:00:00 -0500
category: "{data['category']}"
author: "{data['author']}"
hero_image: "/assets/images/week{week_num}-hero.jpg"
excerpt: "{data['excerpt']}"
---

{data['content']['opening_hook']}

---

## {data['content']['section_1_title']}

{data['content']['section_1_text']}

---

## {data['content']['section_2_title']}

{data['content']['section_2_text']}

---

## {data['content']['section_3_title']}

{data['content']['section_3_text']}

---

## {data['content']['section_4_title']}

{data['content']['section_4_text']}

---

## Your Next Step

{data['content']['closing']}
"""

    # Write post
    output_path = f'_posts/{date_str}-{slug}.md'
    with open(output_path, 'w') as f:
        f.write(md)

    # Copy hero image
    src_img = f'assets/hero-images/week-{week_num:02d}-hero.jpg'
    dst_img = f'assets/images/week{week_num}-hero.jpg'
    if os.path.exists(src_img) and not os.path.exists(dst_img):
        import shutil
        shutil.copy(src_img, dst_img)

    print(f"✓ Week {week_num}: {output_path}")

# Generate weeks 15-52
for week in range(15, 53):
    try:
        convert_week_to_post(week)
    except Exception as e:
        print(f"✗ Week {week}: {e}")
```

## Gemini Prompt
```
You are converting ModelIt K-12 newsletter content from JSON to Jekyll markdown.

For each week 15-52:
1. Read content/week-json/week-{NN}-content.json
2. Generate _posts/{date}-{slug}.md using the template above
3. Copy hero image from assets/hero-images/ to assets/images/

Follow the exact markdown format specified. Preserve all content exactly.
Generate all 38 posts in one batch.
```

## Validation Checklist
After generation, verify:
- [ ] 38 new files in `_posts/` (weeks 15-52)
- [ ] All files have valid front matter (title, date, category, hero_image)
- [ ] All hero images copied to `assets/images/`
- [ ] `bundle exec jekyll build` succeeds locally
- [ ] Push to GitHub and verify pages deploy

## Quick Start for Gemini
```bash
cd ~/repos/modelitk12-blog
python3 scripts/batch_generate_posts.py  # After creating the script
git add _posts/ assets/images/
git commit -m "Add weeks 15-52 blog posts (batch generated)"
git push origin master
```

## Notes
- All 52 hero images already exist in `assets/hero-images/`
- Content quality is high - already written by AI with human review
- Bi-weekly publishing can be configured after all posts exist
