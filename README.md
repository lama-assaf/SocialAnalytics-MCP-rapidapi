<h1 align="center">Social Media Scraper - Custom MCP Server</h1>

A comprehensive Model Context Protocol (MCP) server that provides social media scraping capabilities for LinkedIn, Facebook, Instagram, and Google search functionality.

## What is MCP?

**[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)** is an open standard that enables AI assistants to securely connect with external data sources and tools. MCP servers act as bridges between AI models and various services, allowing for enhanced capabilities like real-time data access, API integrations, and custom tool execution.

## Features
This server exposes comprehensive social media analytics tools for AI assistants:

### LinkedIn Analytics (16 Tools)
- **Profile Analytics**: Personal and company profile data with engagement metrics
- **Content Analytics**: Posts, comments, reactions, and engagement analysis
- **Network Analytics**: Company posts, job market insights, and search capabilities
- **Performance Tracking**: Profile reactions, post reposts, and interaction patterns

### Facebook Analytics
- **Profile Intelligence**: Public profile data with follower insights
- **Engagement Metrics**: Activity patterns and audience interaction data
- **Content Analysis**: Profile engagement and reach analytics

### Instagram Analytics
- **Profile Performance**: Comprehensive profile data with follower demographics
- **Growth Analytics**: Follower count trends and engagement rates
- **Content Insights**: Profile activity and audience interaction patterns

### Web Intelligence
- **Google Search**: Advanced web searches with location and pagination support
- **Competitive Analysis**: Search competitor mentions and market trends

## Installation

### Step 1: Adding MCP to your Python project

If you haven't created a uv-managed project yet, create one:

```bash
uv init custom-mcp-server
cd custom-mcp-server
```

### Step 2: Install MCP Dependencies

Then add MCP to your project dependencies:

```bash
uv add "mcp[cli]"
```
This will auto-generate files and folders similar to the project structure mentioned below, also create a .env file to securely store the API keys.

### Step 3: Add Project Code

In the files generated look for main.py and copy paste the code given in main.py (repo).

### Step 4: Install Additional Dependencies

```bash
uv add httpx python-dotenv fastmcp
```

## Environment Configuration

### Step 1: API Keys Setup

1. **RapidAPI Key**: 
   - Sign up at [RapidAPI](https://rapidapi.com/)
   - Subscribe to the following APIs (Most Important):
     - LinkedIn Scraper API (Real-time & Fast & Affordable): https://rapidapi.com/karimgreek/api/linkedin-scraper-api-real-time-fast-affordable
     - Facebook Scraper3: https://rapidapi.com/krasnoludkolo/api/facebook-scraper3
     - Instagram Scraper Stable API: https://rapidapi.com/thetechguy32744/api/instagram-scraper-stable-api

2. **Google Serper API Key**:
   - Sign up at [Serper.dev](https://serper.dev/)
   - Get your API key from the dashboard

### Step 2: Environment Variables

Create `.env` file in your project root with the following variables:

```env
RAPIDAPI_KEY=your_rapidapi_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## Usage

### Running with Claude Desktop

#### Step 1: Install the Server

You can install this server in [Claude Desktop](https://claude.ai/download) and interact with it right away by running:

```bash
uv run mcp install main.py
```

#### Step 2: Verify Installation

Later, go to Claude AI (desktop version) and you will see changes in the platform similar to the [screenshot shown](https://github.com/Sharan-Kumar-R/Custom-MCP-Server/blob/main/Claude_View.png).

#### Step 3: Start Using the Tools

Paste the URLs of required platform and ask the AI to provide information of the mentioned URLs.

### Analytics Use Cases & Examples

#### 🔍 Competitive Intelligence
```
Analyze competitor engagement: Get all posts and reactions for https://linkedin.com/company/competitor-name
```

```
Track competitor hiring: Search jobs posted by https://linkedin.com/company/competitor-name
```

#### 📊 Content Performance Analysis
```
Analyze top-performing content: Get posts and engagement data for https://linkedin.com/in/industry-leader
```

```
Monitor brand mentions: Search LinkedIn posts containing "your-brand-name"
```

#### 👥 Audience Insights
```
Profile audience analysis: Get follower demographics for https://facebook.com/your-company-page
```

```
Influencer analysis: Get Instagram profile metrics for @influencer-username
```

#### 📈 Social Media Monitoring
```
Track brand sentiment: Get recent posts and comments mentioning "your-company"
```

```
Monitor industry trends: Search posts with keywords "artificial intelligence trends 2024"
```

#### 🎯 Lead Generation
```
Identify prospects: Get company employee profiles from https://linkedin.com/company/target-company
```

```
Research decision makers: Get profile details for https://linkedin.com/in/ceo-name
```

#### 📱 Cross-Platform Analytics
```
Compare social presence: Analyze Instagram @brand vs Facebook /brand-page engagement
```

```
Content strategy insights: Track post performance across LinkedIn company page and executive profiles
```

## Troubleshooting

### MCP Installation Issues

If the MCP tools don't appear in Claude Desktop:

#### Step 1: End Claude Processes
- Windows: Open Task Manager (Ctrl+Shift+Esc)
- Mac: Open Activity Monitor
- End all Claude-related processes

#### Step 2: Reinstall the Server
```bash
uv run mcp install main.py
```

#### Step 3: Restart Claude Desktop
Paste the URLs of required platform and ask the AI to provide information of the mentioned URLs.

### Analytics Data Collection Issues

#### Rate Limiting
If you encounter rate limiting errors:
- Wait 60 seconds between requests for the same platform
- Use different API endpoints to distribute load
- Consider upgrading RapidAPI subscription for higher limits

#### Incomplete Data Returns
For missing analytics data:
- Verify profile/page is public and accessible
- Check if account has privacy restrictions
- Some metrics may require business/creator account access

#### Facebook/Instagram Access Issues
- Ensure profiles are public business pages
- Personal profiles may have limited data availability
- Some engagement metrics require page admin access

#### LinkedIn Premium Data
- Advanced analytics may require LinkedIn Premium URLs
- Company data depends on public visibility settings
- Employee lists limited by company privacy settings

### Testing with MCP Inspector

For development and debugging:

```bash
uv run mcp dev main.py
```

### API Key Validation

Test your API keys independently:

```bash
# Test RapidAPI connection
curl -H "x-rapidapi-key: YOUR_KEY" \
     -H "x-rapidapi-host: linkedin-scraper-api-real-time-fast-affordable.p.rapidapi.com" \
     "https://linkedin-scraper-api-real-time-fast-affordable.p.rapidapi.com/profile/detail?username=test"

# Test Serper API
curl -X POST "https://google.serper.dev/search" \
     -H "X-API-KEY: YOUR_SERPER_KEY" \
     -d '{"q":"test query"}'
```

## Project Structure

```
custom-mcp-server/
├── __pycache__/          # Python bytecode cache (auto-generated)
├── .venv/                # Virtual environment directory
├── .env                  # Environment variables (API keys)
├── .python-version       # Python version specification
├── main.py               # Main MCP server implementation
├── pyproject.toml        # Project configuration and dependencies
├── README.md             # Project documentation
└── uv.lock               # UV lock file for reproducible builds
```

## Analytics Data Examples

### Facebook Profile Analytics Response
```json
{
  "profile": {
    "name": "Tech Company Inc",
    "followers": "125,432",
    "likes": "98,765",
    "about": "Leading technology solutions...",
    "website": "https://techcompany.com",
    "category": "Technology Company",
    "location": "San Francisco, CA",
    "page_transparency": {
      "ads_running": true,
      "created_date": "2018-03-15"
    }
  },
  "engagement_metrics": {
    "average_post_engagement": "2.3%",
    "post_frequency": "Daily",
    "audience_demographics": "Tech professionals, 25-45 years"
  }
}
```

### Instagram Profile Analytics Response
```json
{
  "profile": {
    "username": "tech_influencer",
    "display_name": "Tech Innovator",
    "bio": "AI & Tech Trends | 100K+ followers",
    "followers": 156789,
    "following": 892,
    "posts": 1247,
    "verified": true,
    "profile_pic_url": "https://...",
    "external_url": "https://techblog.com"
  },
  "analytics": {
    "engagement_rate": "4.2%",
    "avg_likes_per_post": 6543,
    "avg_comments_per_post": 234,
    "posting_frequency": "3-4 times per week",
    "top_hashtags": ["#AI", "#tech", "#innovation"]
  }
}
```

### LinkedIn Content Analytics Response
```json
{
  "post_data": {
    "content": "Excited to share our Q4 results...",
    "reactions": {
      "total": 1842,
      "likes": 1234,
      "celebrates": 456,
      "insights": 152
    },
    "comments": 89,
    "shares": 234,
    "engagement_rate": "5.7%",
    "reach": "32,456 impressions"
  },
  "audience_insights": {
    "top_industries": ["Technology", "Finance", "Consulting"],
    "seniority_levels": ["Manager", "Director", "VP"],
    "company_sizes": ["1001-5000", "5001-10000"]
  }
}
```

All data is returned as readable JSON when using Claude Desktop for easy analysis and insights extraction.

## Context Window Optimization

To prevent MCP context window overload, this server implements intelligent data filtering:

### Response Size Controls
- **LinkedIn Profiles**: Limited to ~6KB of essential data (name, title, connections, current role)
- **LinkedIn Posts**: Maximum 5 posts per request, ~5KB limit with key engagement metrics
- **Facebook/Instagram**: Limited to ~4KB focusing on follower counts and engagement rates
- **Search Results**: Maximum 8 results per query with truncated content

### Data Filtering Strategy
- **Excluded Fields**: Profile images, media URLs, full work histories, nested user objects
- **Text Truncation**: Long descriptions limited to 300-500 characters
- **List Limits**: Maximum 10 items in any array (comments, posts, connections)
- **Essential Focus**: Only analytics-relevant metrics and engagement data retained

### Customization
Modify response limits in `main.py`:
```python
RESPONSE_LIMITS = {
    "linkedin_profile": 6000,    # Characters
    "linkedin_posts": 5000,      # Characters  
    "max_posts_returned": 5,     # Number of posts
    "max_comments_returned": 10  # Number of comments
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

In case of any queries, please leave a message or contact me via the email provided in my profile.

<p align="center">
⭐ <strong>Star this repository if you found it helpful!</strong>
</p>
