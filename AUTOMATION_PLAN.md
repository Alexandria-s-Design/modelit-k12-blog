# ModelIt K12 Blog Automation - Complete Implementation Plan

## 🎯 Overview

**Purpose**: Automated weekly blog content generation, publishing, and social media distribution for ModelIt K12

**Approval Workflow**: All content is reviewed and approved via Monday.com before publishing

**Platforms**: GitHub Pages (blog) + 12 social media platforms via Ayrshare

---

## 📋 Monday.com Structure

### **Workspace**: ModelIt Automation Hub
- **ID**: `13222983`
- **Purpose**: Central command center for all ModelIt automations

### **Board 1: Blog Content Pipeline** (ID: `18371710717`)
**Columns**:
- Week (numbers)
- Project (dropdown) - Values: ModelIt K12, Cell Collective
- Publish Date (date)
- Category (dropdown) - Values: Platform Features, Behind the Science, NGSS Standards, Teacher Stories
- Status (status) - Values: Draft → Review → Approved → Published
- Local Preview (link)
- Published URL (link)
- Notes (long_text)

**Workflow**:
1. Thursday 6 PM: Automation creates new item with status "Draft"
2. You review content and change status to "Approved"
3. Automation detects approval and publishes to GitHub + social media
4. Status changes to "Published" with URL links

### **Board 2: Social Media Schedule** (ID: `18371710865`)
**Columns**:
- Post Date (date)
- Project (dropdown) - Values: ModelIt K12, Cell Collective
- Platform (dropdown) - Values: Facebook, LinkedIn, X, Instagram, Pinterest, Bluesky, Reddit, Snapchat, Threads, TikTok, YouTube, GMB
- Post Type (dropdown) - Values: Blog Announcement, Featured Content, Weekly Tip, Student Spotlight
- Post Copy (long_text)
- Media Link (link)
- Blog Link (link)
- Status (status) - Values: Scheduled → Posted → Analytics Collected
- Ayrshare ID (text)
- Reach (numbers)
- Engagement (numbers)
- Clicks (numbers)

**Workflow**:
1. After blog publishes, automation creates social media items for each platform
2. Posts are scheduled and sent to Ayrshare
3. Ayrshare ID is recorded for tracking
4. Monday 9 AM: Analytics collected and metrics updated

### **Board 3: Analytics Dashboard** (ID: `18371710897`)
**Columns**:
- Week (numbers)
- Date Range (text)
- Project (dropdown) - Values: ModelIt K12, Cell Collective
- Blog Post (link)
- Total Reach (numbers)
- Total Engagement (numbers)
- Total Clicks (numbers)
- Page Views (numbers)
- Best Platform (text)
- Performance Notes (long_text)

**Workflow**:
1. Monday 9 AM: Automation aggregates previous week's metrics
2. Creates analytics summary item
3. Identifies best-performing platform and content type

---

## 🗓️ 10-Week Content Calendar

### **Week 3: NGSS Standards Spotlight** (Nov 17, 2025)
- **Category**: NGSS Standards
- **Topics**: MS-LS1-2, MS-LS1-3 alignment, assessment rubrics
- **CTA**: Download free NGSS alignment guide

### **Week 4: Teacher Success Story** (Nov 24, 2025)
- **Category**: Teacher Stories
- **Topics**: Real classroom implementation, student engagement data
- **CTA**: Share your story for feature

### **Week 5: Platform Deep Dive** (Dec 1, 2025)
- **Category**: Platform Features
- **Topics**: Advanced simulation features, custom model building
- **CTA**: Request platform demo

### **Week 6: Research Spotlight** (Dec 8, 2025)
- **Category**: Behind the Science
- **Topics**: Latest Cell Collective publication, research impact
- **CTA**: Explore full research library

### **Week 7: Holiday Implementation Guide** (Dec 15, 2025)
- **Category**: NGSS Standards
- **Topics**: Winter break activities, independent student projects
- **CTA**: Download holiday activity pack

### **Week 8: Year-End Reflection** (Dec 22, 2025)
- **Category**: Teacher Stories
- **Topics**: 2025 highlights, impact metrics, community growth
- **CTA**: Join teacher community forum

### **Week 9: New Year Planning** (Dec 29, 2025)
- **Category**: Platform Features
- **Topics**: Q2 curriculum planning, new features roadmap
- **CTA**: Schedule Q2 planning session

### **Week 10: Advanced Modeling Techniques** (Jan 5, 2026)
- **Category**: Platform Features
- **Topics**: Boolean logic, network analysis, advanced simulations
- **CTA**: Request advanced training webinar

### **Week 11: Cell Collective Integration** (Jan 12, 2026)
- **Category**: Behind the Science
- **Topics**: University research meets K-12, validated models
- **CTA**: Explore Cell Collective platform

### **Week 12: Assessment Strategies** (Jan 19, 2026)
- **Category**: NGSS Standards
- **Topics**: Performance tasks, formative assessment, grading rubrics
- **CTA**: Download assessment toolkit

---

## 🤖 Automation Scripts

### **Directory Structure**
```
/home/claudeuser/workspace/modelitk12-newsletter/
├── automation/
│   ├── config/
│   │   ├── monday_config.json
│   │   ├── ayrshare_config.json
│   │   └── content_calendar.json
│   ├── clients/
│   │   ├── monday_client.py
│   │   ├── ayrshare_client.py
│   │   ├── openrouter_client.py
│   │   └── gemini_client.py
│   ├── workflows/
│   │   ├── orchestrator.py
│   │   ├── generate_content.py
│   │   ├── generate_images.py
│   │   ├── publish_to_github.py
│   │   ├── share_social.py
│   │   ├── check_approvals.py
│   │   └── collect_analytics.py
│   └── logs/
├── drafts/
│   └── week-{N}-{slug}.md
└── _posts/
    └── YYYY-MM-DD-{slug}.md
```

### **Configuration Files**

#### `automation/config/monday_config.json`
```json
{
  "workspace": {
    "id": "13222983",
    "name": "ModelIt Automation Hub"
  },
  "boards": {
    "content_pipeline": {
      "id": "18371710717",
      "name": "Blog Content Pipeline",
      "columns": {
        "week": "numeric_mkxje89w",
        "project": "dropdown_mkxj1f00",
        "publish_date": "date_mkxjh99a",
        "category": "dropdown_mkxj43g0",
        "status": "color_mkxjmjnc",
        "local_preview": "link_mkxjg8s1",
        "published_url": "link_mkxjvp0z",
        "notes": "long_text_mkxj3syg"
      }
    },
    "social_schedule": {
      "id": "18371710865",
      "name": "Social Media Schedule",
      "columns": {
        "post_date": "date_mkxjzp1v",
        "project": "dropdown_mkxjbg01",
        "platform": "dropdown_mkxjpbtx",
        "post_type": "dropdown_mkxjnyyz",
        "post_copy": "long_text_mkxjzxjp",
        "media_link": "link_mkxjmkqt",
        "blog_link": "link_mkxj18k0",
        "status": "color_mkxjffpg",
        "ayrshare_id": "text_mkxjxrv9",
        "reach": "numeric_mkxj2b8t",
        "engagement": "numeric_mkxjrybt",
        "clicks": "numeric_mkxjzje5"
      }
    },
    "analytics_dashboard": {
      "id": "18371710897",
      "name": "Analytics Dashboard",
      "columns": {
        "week": "numeric_mkxjcybk",
        "date_range": "text_mkxjjtd8",
        "project": "dropdown_mkxjg1be",
        "blog_post": "link_mkxjcqhj",
        "total_reach": "numeric_mkxj4e2f",
        "total_engagement": "numeric_mkxjmsb6",
        "total_clicks": "numeric_mkxjc3g7",
        "page_views": "numeric_mkxjce2n",
        "best_platform": "text_mkxj1bpb",
        "performance_notes": "long_text_mkxjaxgw"
      }
    }
  },
  "api_key": "${MONDAY_API_KEY}"
}
```

#### `automation/config/ayrshare_config.json`
```json
{
  "api_key": "${AYRSHARE_API_KEY}",
  "plan": "Business 150",
  "quota": {
    "total_posts_per_month": 1000,
    "reserved_for_modelit": 800,
    "reserved_for_other": 200
  },
  "platforms": {
    "facebook": {
      "enabled": true,
      "post_time": "08:00",
      "profile_key": "modelitk12-facebook"
    },
    "linkedin": {
      "enabled": true,
      "post_time": "09:00",
      "profile_key": "modelitk12-linkedin"
    },
    "x": {
      "enabled": true,
      "post_time": "10:00",
      "profile_key": "modelitk12-twitter"
    },
    "instagram": {
      "enabled": false,
      "post_time": "11:00",
      "profile_key": "modelitk12-instagram"
    },
    "pinterest": {
      "enabled": false,
      "post_time": "12:00"
    },
    "bluesky": {
      "enabled": false,
      "post_time": "13:00"
    },
    "reddit": {
      "enabled": false,
      "post_time": "14:00"
    },
    "snapchat": {
      "enabled": false,
      "post_time": "15:00"
    },
    "threads": {
      "enabled": false,
      "post_time": "16:00"
    },
    "tiktok": {
      "enabled": false,
      "post_time": "17:00"
    },
    "youtube": {
      "enabled": false,
      "post_time": "18:00"
    },
    "gmb": {
      "enabled": false,
      "post_time": "19:00"
    }
  },
  "hashtags": {
    "modelit_k12": "#ModelItK12 #ScienceEducation #NGSS #SystemsThinking #CellCollective",
    "cell_collective": "#CellCollective #SystemsBiology #ComputationalBiology #Research"
  },
  "tags": {
    "project": "modelit_k12",
    "source": "automation",
    "content_type": "blog_announcement"
  }
}
```

---

## 🔧 Implementation Details

### **Phase 1: Client Libraries** (Week 1)

#### `automation/clients/monday_client.py`
```python
#!/usr/bin/env python3
"""
Monday.com GraphQL API Client
Handles all interactions with Monday.com workspace
"""

import os
import json
import requests
from pathlib import Path
from typing import Dict, List, Optional

class MondayClient:
    def __init__(self, config_path: str = None):
        if config_path:
            with open(config_path) as f:
                config = json.load(f)
                self.api_key = config['api_key']
                self.workspace_id = config['workspace']['id']
                self.boards = config['boards']
        else:
            self.api_key = os.getenv('MONDAY_API_KEY')
            self.workspace_id = "13222983"

        self.endpoint = "https://api.monday.com/v2"
        self.headers = {
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        }

    def execute_query(self, query: str, variables: Dict = None) -> Dict:
        """Execute GraphQL query"""
        payload = {"query": query}
        if variables:
            payload["variables"] = variables

        response = requests.post(
            self.endpoint,
            json=payload,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def create_item(self, board_id: str, item_name: str, column_values: Dict) -> str:
        """Create new item in board"""
        query = """
        mutation ($board_id: ID!, $item_name: String!, $column_values: JSON!) {
          create_item(
            board_id: $board_id,
            item_name: $item_name,
            column_values: $column_values
          ) {
            id
          }
        }
        """

        variables = {
            "board_id": board_id,
            "item_name": item_name,
            "column_values": json.dumps(column_values)
        }

        result = self.execute_query(query, variables)
        return result['data']['create_item']['id']

    def update_item(self, item_id: str, board_id: str, column_values: Dict):
        """Update existing item"""
        query = """
        mutation ($board_id: ID!, $item_id: ID!, $column_values: JSON!) {
          change_multiple_column_values(
            board_id: $board_id,
            item_id: $item_id,
            column_values: $column_values
          ) {
            id
          }
        }
        """

        variables = {
            "board_id": board_id,
            "item_id": item_id,
            "column_values": json.dumps(column_values)
        }

        self.execute_query(query, variables)

    def get_items_by_status(self, board_id: str, status: str) -> List[Dict]:
        """Get all items with specific status"""
        query = """
        query ($board_id: ID!) {
          boards(ids: [$board_id]) {
            items_page {
              items {
                id
                name
                column_values {
                  id
                  text
                  value
                }
              }
            }
          }
        }
        """

        variables = {"board_id": board_id}
        result = self.execute_query(query, variables)

        items = result['data']['boards'][0]['items_page']['items']

        # Filter by status
        filtered_items = []
        for item in items:
            for col in item['column_values']:
                if col['id'] == 'status' and status.lower() in col['text'].lower():
                    filtered_items.append(item)
                    break

        return filtered_items

    def change_status(self, item_id: str, board_id: str, status_column_id: str, status_label: str):
        """Change item status"""
        column_values = {
            status_column_id: {"label": status_label}
        }
        self.update_item(item_id, board_id, column_values)

# Example usage
if __name__ == "__main__":
    client = MondayClient()

    # Create blog content item
    item_id = client.create_item(
        board_id="18371710717",
        item_name="Week 3: NGSS Standards Spotlight",
        column_values={
            "numeric_mkxje89w": 3,  # Week
            "dropdown_mkxj1f00": {"labels": ["ModelIt K12"]},  # Project
            "date_mkxjh99a": {"date": "2025-11-17"},  # Publish Date
            "dropdown_mkxj43g0": {"labels": ["NGSS Standards"]},  # Category
            "color_mkxjmjnc": {"label": "Draft"}  # Status
        }
    )

    print(f"Created item: {item_id}")
```

#### `automation/clients/ayrshare_client.py`
```python
#!/usr/bin/env python3
"""
Ayrshare API Client
Handles multi-platform social media posting and analytics
"""

import os
import json
import requests
from typing import Dict, List, Optional
from datetime import datetime

class AyrshareClient:
    def __init__(self, config_path: str = None):
        if config_path:
            with open(config_path) as f:
                config = json.load(f)
                self.api_key = config['api_key']
                self.platforms = config['platforms']
                self.hashtags = config['hashtags']
                self.tags = config['tags']
        else:
            self.api_key = os.getenv('AYRSHARE_API_KEY')

        self.base_url = "https://app.ayrshare.com/api"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def post(self,
             post_text: str,
             platforms: List[str],
             media_urls: List[str] = None,
             schedule_time: datetime = None,
             tags: Dict = None) -> Dict:
        """
        Post content to multiple social media platforms

        Args:
            post_text: Content to post
            platforms: List of platform names (facebook, linkedin, x, etc.)
            media_urls: Optional list of image/video URLs
            schedule_time: Optional datetime to schedule post
            tags: Optional metadata tags for analytics tracking

        Returns:
            Response dict with post IDs for each platform
        """
        payload = {
            "post": post_text,
            "platforms": platforms
        }

        if media_urls:
            payload["mediaUrls"] = media_urls

        if schedule_time:
            payload["scheduleDate"] = schedule_time.isoformat()

        if tags:
            payload["tags"] = tags
        else:
            payload["tags"] = self.tags

        response = requests.post(
            f"{self.base_url}/post",
            json=payload,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def get_analytics(self, post_id: str) -> Dict:
        """Get analytics for a specific post"""
        response = requests.get(
            f"{self.base_url}/analytics/post/{post_id}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def get_analytics_by_tags(self, tags: Dict, start_date: str, end_date: str) -> List[Dict]:
        """Get analytics for posts with specific tags in date range"""
        params = {
            "tags": json.dumps(tags),
            "startDate": start_date,
            "endDate": end_date
        }

        response = requests.get(
            f"{self.base_url}/analytics/tags",
            params=params,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def get_profiles(self) -> Dict:
        """Get all connected social media profiles"""
        response = requests.get(
            f"{self.base_url}/profiles",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

# Example usage
if __name__ == "__main__":
    client = AyrshareClient()

    # Post to Facebook, LinkedIn, and X
    result = client.post(
        post_text="🔬 NEW BLOG: Discover how ModelIt! K12 aligns with NGSS standards!\n\nLearn how computational modeling meets middle school science education.\n\nRead more: https://charlesmartinedd.github.io/modelitk12-newsletter/\n\n#ModelItK12 #NGSS #ScienceEducation",
        platforms=["facebook", "linkedin", "twitter"],
        media_urls=["https://charlesmartinedd.github.io/modelitk12-newsletter/assets/images/week3-hero.jpg"],
        tags={
            "project": "modelit_k12",
            "content_type": "blog_announcement",
            "week": 3
        }
    )

    print(f"Posted successfully: {result}")
```

#### `automation/clients/openrouter_client.py`
```python
#!/usr/bin/env python3
"""
OpenRouter API Client
Handles GPT-5 content generation
"""

import os
import requests
from typing import Dict, List

class OpenRouterClient:
    def __init__(self):
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        self.base_url = "https://openrouter.ai/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://charlesmartinedd.github.io/modelitk12-newsletter/",
            "X-Title": "ModelIt K12 Blog Generator"
        }

    def generate_blog_post(self,
                          week_number: int,
                          category: str,
                          topics: List[str],
                          cta: str,
                          existing_posts: List[str] = None) -> str:
        """
        Generate complete blog post using GPT-5

        Args:
            week_number: Week number in series
            category: Content category (Platform Features, Behind the Science, etc.)
            topics: List of topics to cover
            cta: Call-to-action for end of post
            existing_posts: Optional list of previous post content for style matching

        Returns:
            Complete blog post markdown content
        """

        system_prompt = """You are an expert educational content writer for ModelIt! K12,
        a systems modeling platform for middle school science education. Your writing style is:

        - Clear, engaging, and accessible to middle school science teachers
        - Research-backed with specific data and examples
        - Practical with actionable classroom strategies
        - Enthusiastic about computational biology and systems thinking
        - Professional but conversational

        Always include:
        - Real classroom examples
        - Specific NGSS standard alignments when relevant
        - Step-by-step implementation guides
        - Research citations from Cell Collective publications
        - Clear CTAs that encourage teacher engagement

        Format: Jekyll markdown with YAML frontmatter
        """

        user_prompt = f"""Generate Week {week_number} blog post for "The Systems Thinker's Weekly"

        Category: {category}
        Topics to cover: {', '.join(topics)}
        Call-to-action: {cta}

        Requirements:
        - Title should be compelling and SEO-friendly
        - Excerpt must be 1-2 sentences summarizing key value
        - Content should be 1500-2000 words
        - Include practical classroom examples
        - Reference specific Cell Collective models when relevant
        - Use subheadings for scannability
        - End with clear CTA and preview of next week

        Maintain consistency with existing blog voice and structure.
        """

        payload = {
            "model": "openai/gpt-5",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 4000
        }

        response = requests.post(
            f"{self.base_url}/chat/completions",
            json=payload,
            headers=self.headers
        )
        response.raise_for_status()

        result = response.json()
        return result['choices'][0]['message']['content']

# Example usage
if __name__ == "__main__":
    client = OpenRouterClient()

    blog_content = client.generate_blog_post(
        week_number=3,
        category="NGSS Standards",
        topics=[
            "MS-LS1-2 alignment with ModelIt",
            "MS-LS1-3 systems interactions",
            "Assessment rubrics for modeling activities",
            "Classroom implementation strategies"
        ],
        cta="Download free NGSS alignment guide"
    )

    print(blog_content)
```

---

## 🚀 Workflow Scripts

### `automation/workflows/orchestrator.py`
**Purpose**: Master control script that coordinates entire automation workflow

**Key Functions**:
- Weekly content generation trigger (Thursday 6 PM)
- Approval monitoring (every 15 minutes)
- Analytics collection (Monday 9 AM)
- Error handling and logging

### `automation/workflows/generate_content.py`
**Purpose**: Generate blog post content and hero images

**Process**:
1. Load content calendar for current week
2. Generate blog content via GPT-5
3. Generate hero image via Gemini
4. Save draft to `drafts/` directory
5. Create Monday.com item in Blog Content Pipeline
6. Set status to "Draft" for your review

### `automation/workflows/check_approvals.py`
**Purpose**: Poll Monday.com for approved content

**Process**:
1. Query Blog Content Pipeline for items with status "Approved"
2. For each approved item:
   - Trigger `publish_to_github.py`
   - Trigger `share_social.py`
   - Update status to "Published"
   - Record published URL

### `automation/workflows/publish_to_github.py`
**Purpose**: Publish approved blog posts to GitHub Pages

**Process**:
1. Move draft from `drafts/` to `_posts/` with proper filename
2. Git add, commit, push to GitHub
3. Wait for GitHub Actions to rebuild site
4. Verify published URL is live
5. Update Monday.com with published URL

### `automation/workflows/share_social.py`
**Purpose**: Distribute blog content across social media platforms

**Process**:
1. Generate platform-specific post copy
2. Schedule posts via Ayrshare to enabled platforms
3. Create Monday.com items in Social Media Schedule for each post
4. Record Ayrshare post IDs for analytics tracking

### `automation/workflows/collect_analytics.py`
**Purpose**: Aggregate performance metrics weekly

**Process**:
1. Query Ayrshare for analytics on all posts from previous week
2. Aggregate metrics by platform and content type
3. Create summary item in Analytics Dashboard
4. Update Social Media Schedule items with metrics
5. Generate performance insights

---

## ⏰ Cron Schedule

```bash
# Content generation - Every Thursday at 6 PM
0 18 * * 4 /usr/bin/python3 /home/claudeuser/workspace/modelitk12-newsletter/automation/workflows/generate_content.py >> /home/claudeuser/workspace/modelitk12-newsletter/automation/logs/generation.log 2>&1

# Approval monitoring - Every 15 minutes
*/15 * * * * /usr/bin/python3 /home/claudeuser/workspace/modelitk12-newsletter/automation/workflows/check_approvals.py >> /home/claudeuser/workspace/modelitk12-newsletter/automation/logs/approvals.log 2>&1

# Analytics collection - Every Monday at 9 AM
0 9 * * 1 /usr/bin/python3 /home/claudeuser/workspace/modelitk12-newsletter/automation/workflows/collect_analytics.py >> /home/claudeuser/workspace/modelitk12-newsletter/automation/logs/analytics.log 2>&1
```

---

## 🔄 Expandability

This system is designed for easy expansion. To add new automations:

### **Adding New Content Types**
1. Add new category to Blog Content Pipeline dropdown
2. Update content calendar template
3. Extend GPT-5 prompts in `generate_content.py`

### **Adding New Social Platforms**
1. Enable platform in Ayrshare dashboard
2. Update `ayrshare_config.json` with platform settings
3. Add platform to Social Media Schedule dropdown
4. Update `share_social.py` to include new platform

### **Adding New Projects** (beyond ModelIt)
1. Add project to Project dropdown in all boards
2. Create separate Ayrshare tags for analytics segmentation
3. Create separate content calendars
4. Extend orchestrator to handle multiple projects

### **Adding New Automation Workflows**
1. Create new board in Monday.com Automation Hub workspace
2. Write new workflow script in `automation/workflows/`
3. Add cron job for scheduling
4. Update orchestrator to monitor new board

---

## 🎓 Next Steps

1. **Review Monday.com boards**: https://monday.com/boards/13222983
2. **Approve configuration files** above
3. **I'll create all automation scripts**
4. **Test Week 3 content generation**
5. **Deploy cron jobs**
6. **Go live!**

---

**Questions or modifications needed?** Let me know and I'll adjust the plan accordingly.
