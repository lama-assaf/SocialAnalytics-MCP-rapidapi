# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Model Context Protocol (MCP) server that provides social media scraping capabilities for LinkedIn, Facebook, Instagram, and Google search functionality. The server exposes tools for AI assistants to access external social media data through various APIs.

## Key Commands

### Development
- `uv run main.py` - Run the MCP server directly
- `uv run mcp dev main.py` - Run with MCP Inspector for testing
- `uv run mcp install main.py` - Install the server to Claude Desktop

### Package Management
- `uv add <package>` - Add new dependencies
- `uv lock` - Update the lock file
- `uv sync` - Sync dependencies from lock file

### Troubleshooting
If MCP tools don't appear in Claude Desktop:
1. End all Claude processes (Task Manager/Activity Monitor)
2. Reinstall: `uv run mcp install main.py`
3. Restart Claude Desktop completely

## Architecture

### Core Components

**main.py** - Main MCP server implementation containing:
- FastMCP server initialization
- **16 LinkedIn tools** (complete API coverage):
  - `get_personal_profile(linkedin_url: str)` - LinkedIn personal profiles
  - `get_company_profile(linkedin_url: str)` - LinkedIn company pages
  - `get_profile_posts(linkedin_url: str)` - User's recent posts
  - `get_profile_comments(linkedin_url: str)` - User's recent comments
  - `get_profile_reactions(linkedin_url: str)` - User's recent reactions
  - `get_post_comments(post_url: str)` - Post comments & engagement
  - `get_post_details(post_url: str)` - Detailed post information
  - `get_post_reactions(post_url: str)` - Post reactions data
  - `get_post_reposts(post_url: str)` - Post repost data
  - `search_posts(keyword: str)` - Search posts by keyword
  - `get_company_posts(company_identifier: str)` - Company posts
  - `search_companies(keyword: str)` - Search companies
  - `search_jobs(keyword: str, location: str = "")` - Job search
  - `get_job_details(job_url: str)` - Job posting details
  - `check_api_health()` - API health status
- **Social media tools**:
  - `get_facebook_profile(profile_url: str)` - Facebook public profiles
  - `get_instagram_profile(instagram_url_or_username: str)` - Instagram profiles
- **Web search**:
  - `scrape_website(query: str, gl: str = "in", num: int = 10, page: int = 1)` - Google search via Serper API

### API Integration Pattern

All scraping tools follow a consistent pattern:
1. **Fetch function** - Async HTTP client with error handling
2. **Tool decorator** - MCP tool registration with JSON string return
3. **Headers** - RapidAPI authentication with host-specific headers
4. **Error handling** - Try/catch with descriptive error messages

### Parameter Validation Requirements

**Critical: Always verify parameter names before implementing new endpoints.**

LinkedIn API endpoints use specific parameter names that must be tested:
- Personal profiles: `username` parameter (extract from URLs like `/in/username`)
- Company profiles: `identifier` parameter (accepts URLs, names, or URNs)
- Posts endpoints: `post_url` parameter
- Search endpoints: **Parameter names vary and must be tested individually**

**Testing new parameters:**
```bash
# Test different parameter names for new endpoints
uv run python -c "
import asyncio, httpx, os
from dotenv import load_dotenv

async def test_params(endpoint, test_value, param_names):
    load_dotenv()
    headers = {'x-rapidapi-key': os.getenv('RAPIDAPI_KEY'), 
               'x-rapidapi-host': 'linkedin-scraper-api-real-time-fast-affordable.p.rapidapi.com'}
    
    async with httpx.AsyncClient() as client:
        for param in param_names:
            try:
                response = await client.get(f'https://linkedin-scraper-api-real-time-fast-affordable.p.rapidapi.com{endpoint}',
                                          headers=headers, params={param: test_value}, timeout=10.0)
                print(f'{param}: {response.status_code}')
                if response.status_code == 200: break
            except Exception as e: print(f'{param}: Error')

# Usage: asyncio.run(test_params('/posts/search', 'technology', ['keyword', 'query', 'q']))
"
```

### External APIs Used

- **RapidAPI** - LinkedIn, Facebook, and Instagram scrapers
  - LinkedIn Scraper API (see docs/LinkedIn_Scraper_API_endpoints.md) - Uses `/profile/detail` and `/companies/detail`
  - Facebook Scraper3 (see docs/Facebook_api_endpoints.md)
  - Instagram Scraper Stable API (28+ endpoints available - see docs/Instagram_api_enpoints.md)
  - Fresh LinkedIn Profile Data (alternative API - see docs/FreshLinkedInProfile_api_endpoints.md)
- **Google Serper** - Web search functionality

## Environment Configuration

Required environment variables in `.env`:
```env
RAPIDAPI_KEY=your_rapidapi_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## Development Notes

### Implementation Details
- All HTTP requests use 30-second timeouts
- Error handling returns descriptive messages rather than exceptions
- JSON responses are formatted with 2-space indentation for readability
- The server uses stdio transport for MCP communication
- Single-file architecture (main.py:583 lines) with comprehensive LinkedIn API coverage

### Error Handling Pattern
Each API tool follows consistent error handling:
1. Try/catch blocks around HTTP requests
2. Print error messages to console
3. Return None for failed requests
4. Return "Unable to fetch..." message for tool failures

### API Response Format
All tools return JSON strings with consistent structure:
- Social media tools: Raw API response data as JSON
- Google search: Serper API response format
- Error cases: Descriptive error messages

## Testing Strategy

### Development Testing
Use MCP Inspector for interactive testing:
```bash
uv run mcp dev main.py
```

### Endpoint Verification
Test individual endpoints directly:
```bash
uv run python -c "
import asyncio
import sys
sys.path.append('.')
from main import get_personal_profile, check_api_health

async def test():
    # Test working endpoints
    health = await check_api_health()
    profile = await get_personal_profile('razane-boustany')
    print('Health:', health[:100])
    print('Profile:', profile[:100])

asyncio.run(test())
"
```

### Production Testing
For Claude Desktop integration:
1. Install: `uv run mcp install main.py`
2. Restart Claude Desktop completely
3. Verify MCP tools appear in Claude interface
4. Test with actual URLs/queries

### Endpoint Status
**Verified Working:**
- Personal profiles, company profiles, profile posts
- API health check
- Facebook/Instagram profiles, Google search

**Needs Parameter Verification:**
- Some search endpoints may require different parameter names
- Test new endpoints individually before documenting as functional

### No Formal Test Suite
This project uses manual testing through MCP Inspector and Claude Desktop integration. No unit tests or automated testing framework is implemented.