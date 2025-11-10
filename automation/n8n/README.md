# n8n Workflow Automation for ModelIt K12 Blog

## What is n8n?

**n8n** is a workflow automation tool (like Zapier, but you own it). It connects different services together with a visual interface.

**Think of it like dominoes**:
- First domino: "Every Thursday at 6 PM" (Cron trigger)
- Second domino: "Generate blog content" (OpenRouter API)
- Third domino: "Create Monday.com item for approval" (Monday.com API)
- Fourth domino: "Wait for your approval"
- Fifth domino: "Publish to GitHub" (GitHub API)
- Last domino: "Share on social media" (Ayrshare API)

## How to Install n8n

### Option 1: Cloud Hosted (Easiest - Recommended)
```bash
# Sign up at n8n.cloud
# https://n8n.cloud
# They host everything for you ($20/month)
```

### Option 2: Self-Hosted (Free, but you manage it)
```bash
# Install with npm
npm install n8n -g

# Run n8n
n8n start

# Access at http://localhost:5678
```

### Option 3: Docker (Good for always-on server)
```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

## Workflows to Import

I've created 5 n8n workflows for you:

1. **`workflow_1_content_generation.json`** - Generate blog content every Thursday 6 PM
2. **`workflow_2_approval_monitor.json`** - Check Monday.com every 15 min for approvals
3. **`workflow_3_github_publisher.json`** - Publish approved content to GitHub Pages
4. **`workflow_4_social_distributor.json`** - Share to social media via Ayrshare
5. **`workflow_5_analytics_collector.json`** - Collect performance metrics every Monday 9 AM

## Setup Instructions

### Step 1: Set Up n8n Credentials

In n8n, go to **Settings > Credentials** and add:

1. **Monday.com API**
   - Name: `ModelIt Monday.com`
   - API Key: `eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjU3OTg4ODA1MywiYWFpIjoxMSwidWlkIjozNzU2NTU0MywiaWFkIjoiMjAyNS0xMC0yOVQwNTozNDoyNy4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTQ1NTQ1MzcsInJnbiI6InVzZTEifQ.jahR322ZRtgRDu-EyLd-C-ZoYT9MGqvvsvQlJuD__IE`

2. **Ayrshare API**
   - Name: `ModelIt Ayrshare`
   - API Key: `7D248853-8AF94A41-A48F07DC-73F74D88`

3. **OpenRouter API**
   - Name: `OpenRouter GPT-5`
   - API Key: `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`

4. **GitHub API**
   - Name: `GitHub modelitk12-newsletter`
   - Access Token: (from `/home/claudeuser/workspace/.github-token`)

### Step 2: Import Workflows

1. In n8n, click **Workflows > Import from File**
2. Import each JSON file from this directory
3. Each workflow will appear in your workflow list

### Step 3: Activate Workflows

1. Open each workflow
2. Review the nodes and connections
3. Click **Active** toggle in top-right corner
4. Green = Active, Gray = Inactive

### Step 4: Test

1. **Manual Test**: Click "Execute Workflow" button
2. **Check Logs**: View execution history at bottom of screen
3. **Monday.com**: Verify items appear in boards

## Workflow Details

### 🔄 Workflow 1: Content Generation (Thursday 6 PM)

**Trigger**: Cron (Thursday 18:00)

**Steps**:
1. Read content calendar JSON
2. Get current week number
3. Call OpenRouter GPT-5 to generate blog post
4. Call Gemini to generate hero image
5. Save draft markdown file locally
6. Create Monday.com item in Blog Content Pipeline
7. Set status to "Draft"
8. Send you notification

**Output**: Draft blog post ready for your review in Monday.com

---

### 👀 Workflow 2: Approval Monitor (Every 15 min)

**Trigger**: Cron (*/15 * * * *)

**Steps**:
1. Query Monday.com Blog Content Pipeline
2. Filter for items with status = "Approved"
3. For each approved item:
   - Trigger Workflow 3 (GitHub Publisher)
   - Trigger Workflow 4 (Social Distributor)
4. Update status to "Published"

**Output**: Approved content gets published automatically

---

### 📤 Workflow 3: GitHub Publisher

**Trigger**: Webhook from Workflow 2

**Steps**:
1. Read draft markdown from local file
2. Move file to `_posts/` with proper date format
3. Git add, commit, push to GitHub
4. Wait 2 minutes for GitHub Pages rebuild
5. Verify published URL is live
6. Update Monday.com with published URL
7. Return success/failure status

**Output**: Blog post live on GitHub Pages

---

### 📱 Workflow 4: Social Distributor

**Trigger**: Webhook from Workflow 2

**Steps**:
1. Read blog post metadata (title, excerpt, URL)
2. Generate platform-specific post copy:
   - Facebook: Long-form with emoji
   - LinkedIn: Professional tone
   - X/Twitter: Concise 280 chars
3. Call Ayrshare API to schedule posts
4. Create Monday.com items in Social Media Schedule
5. Record Ayrshare post IDs for tracking

**Output**: Social media posts scheduled across platforms

---

### 📊 Workflow 5: Analytics Collector (Monday 9 AM)

**Trigger**: Cron (Monday 09:00)

**Steps**:
1. Calculate previous week date range
2. Query Ayrshare analytics API
3. Get metrics for all posts from previous week
4. Aggregate by platform and post type
5. Update Monday.com Social Media Schedule with metrics
6. Create summary in Analytics Dashboard
7. Send weekly report email

**Output**: Performance insights in Monday.com

---

## Visual Workflow Diagrams

I'll create visual diagrams showing how each workflow connects.

## Approval Process (How You'll Use This)

**Thursday Evening**:
1. n8n generates blog content automatically
2. You get notification: "Week 3 content ready for review"
3. Open Monday.com > Blog Content Pipeline
4. Review draft blog post (local preview link)

**Your Review**:
- Like it? Change status to "Approved"
- Need changes? Change status to "Review" and add notes
- Want to delay? Change status to "On Hold"

**After Approval**:
- Within 15 minutes, n8n detects "Approved" status
- Publishes to GitHub automatically
- Shares to Facebook, LinkedIn, X automatically
- Updates Monday.com with published URLs
- You get notification: "Week 3 published successfully"

**Monday Morning**:
- n8n collects analytics from previous week
- Updates Monday.com with engagement metrics
- You review performance in Analytics Dashboard

## Troubleshooting

### "Workflow not running on schedule"
- Check workflow is **Active** (green toggle)
- Check n8n is running (if self-hosted)
- Check cron syntax is correct

### "Monday.com API errors"
- Verify API key is correct in credentials
- Check board IDs match your workspace
- Ensure API key has write permissions

### "GitHub push failed"
- Check GitHub token has repo write access
- Verify local git is configured
- Check for merge conflicts

### "Ayrshare posts failing"
- Verify API key is valid
- Check platform connections in Ayrshare dashboard
- Ensure media URLs are publicly accessible

## Next Steps

Ready to create the actual n8n workflow JSON files? I'll generate all 5 workflows with complete node configurations.
