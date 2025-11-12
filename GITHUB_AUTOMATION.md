# GitHub Actions Newsletter Automation

## How It Works

This repository uses GitHub Actions to automatically publish a new newsletter every Sunday at 9:00 AM EST.

### Workflow: `publish-newsletter.yml`

**Schedule**: Every Sunday at 9:00 AM EST (14:00 UTC)

**What it does**:
1. Finds the next draft in `drafts/` directory (lowest week number)
2. Moves it to `_posts/` with current date in filename
3. Commits and pushes the change
4. GitHub Pages automatically rebuilds the site

### File Naming Convention

**Drafts**: `drafts/weekX-title-slug.md`
- Example: `drafts/week3-ngss-standards.md`

**Published**: `_posts/YYYY-MM-DD-title-slug.md`
- Example: `_posts/2025-11-17-ngss-standards.md`

### Publishing Schedule

| Week | Publish Date | Draft File | Status |
|------|--------------|------------|--------|
| Week 1 | Nov 1, 2025 | ✅ Published | Already live |
| Week 2 | Nov 10, 2025 | ✅ Published | Already live |
| Week 3 | Nov 17, 2025 | `week3-ngss-standards.md` | Scheduled |
| Week 4 | Nov 24, 2025 | `week4-platform-deep-dive.md` | Scheduled |
| Week 5 | Dec 1, 2025 | `week5-research-spotlight.md` | Scheduled |
| Week 6 | Dec 8, 2025 | `week6-holiday-implementation.md` | Scheduled |

## Manual Publishing

You can manually trigger the workflow:

1. Go to **Actions** tab in GitHub
2. Select **Publish Weekly Newsletter**
3. Click **Run workflow**
4. Choose branch (usually `main`)
5. Click **Run workflow**

## Testing

To test locally before pushing:

```bash
# Simulate what the workflow does
NEXT_DRAFT=$(ls drafts/week*.md | sort | head -n 1)
PUBLISH_DATE=$(date +%Y-%m-%d)
DRAFT_FILENAME=$(basename "$NEXT_DRAFT")
TITLE_PART=$(echo "$DRAFT_FILENAME" | sed 's/week[0-9]*-//')
NEW_FILENAME="${PUBLISH_DATE}-${TITLE_PART}"

echo "Would move: $NEXT_DRAFT → _posts/$NEW_FILENAME"
```

## Adding New Newsletters

1. Create draft in `drafts/` directory
2. Use naming: `weekX-title-slug.md` (where X is the next number)
3. Include YAML front matter:
   ```yaml
   ---
   layout: post
   title: "Your Title"
   date: YYYY-MM-DD HH:MM:SS -0500
   category: "Category Name"
   author: "Dr. Marie & Charles Martin"
   hero_image: "/assets/images/weekX-hero.jpg"
   excerpt: "Brief description..."
   ---
   ```
4. The workflow will automatically publish on next Sunday

## Troubleshooting

**Workflow not running?**
- Check GitHub Actions is enabled for the repository
- Verify the cron schedule is correct (14:00 UTC = 9:00 AM EST)
- Check the Actions tab for errors

**Wrong file published?**
- Drafts are published in alphabetical order
- Use `week3`, `week4`, etc. to maintain order
- Avoid non-sequential numbering

**Manual override needed?**
- Use the "Run workflow" button in Actions tab
- Or manually move files and commit

## Repository Permissions

The workflow requires:
- ✅ **Read** repository contents
- ✅ **Write** to repository (commit changes)
- ✅ **GITHUB_TOKEN** (automatically provided)

No additional secrets or API keys needed.
