from typing import Any
import httpx
import json
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv

load_dotenv()

# Load API keys from .env
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# API hosts
LINKEDIN_HOST = "linkedin-scraper-api-real-time-fast-affordable.p.rapidapi.com"
FACEBOOK_HOST = "facebook-scraper3.p.rapidapi.com"
INSTAGRAM_HOST = "instagram-scraper-stable-api.p.rapidapi.com"

LINKEDIN_API_BASE = f"https://{LINKEDIN_HOST}"
FACEBOOK_API_BASE = f"https://{FACEBOOK_HOST}"
INSTAGRAM_API_BASE = f"https://{INSTAGRAM_HOST}"
SERPER_API_BASE = "https://google.serper.dev"

# Check required keys
if not RAPIDAPI_KEY:
    raise ValueError("RAPIDAPI_KEY is not set in the environment variables")
if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY is not set in the environment variables")

# Initialize MCP
mcp = FastMCP("social_web_scraper")

# ---- LINKEDIN PERSONAL PROFILE TOOL ----
async def fetch_personal_profile(linkedin_url: str) -> dict[str, Any] | None:
    # Extract username from LinkedIn URL (e.g., "razane-boustany" from "https://www.linkedin.com/in/razane-boustany/")
    if "/in/" in linkedin_url:
        username = linkedin_url.split("/in/")[1].rstrip("/")
    else:
        username = linkedin_url  # assume it's already a username
    params = {"username": username}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/profile/detail",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn personal profile: {e}")
            return None

@mcp.tool()
async def get_personal_profile(linkedin_url: str) -> str:
    """Fetch full LinkedIn personal profile data for a given URL."""
    data = await fetch_personal_profile(linkedin_url)
    if not data:
        return "Unable to fetch LinkedIn personal profile data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN COMPANY PROFILE TOOL ----
async def fetch_company_profile(linkedin_url: str) -> dict[str, Any] | None:
    # The /companies/detail endpoint accepts company name, LinkedIn URL, or URN
    params = {"identifier": linkedin_url}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/companies/detail",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn company profile: {e}")
            return None

@mcp.tool()
async def get_company_profile(linkedin_url: str) -> str:
    """Fetch full LinkedIn company page data for a given URL."""
    data = await fetch_company_profile(linkedin_url)
    if not data:
        return "Unable to fetch LinkedIn company profile data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN PROFILE POSTS TOOL ----
async def fetch_profile_posts(linkedin_url: str) -> dict[str, Any] | None:
    # Extract username from LinkedIn URL
    if "/in/" in linkedin_url:
        username = linkedin_url.split("/in/")[1].rstrip("/")
    else:
        username = linkedin_url
    params = {"username": username}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/profile/posts",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn profile posts: {e}")
            return None

@mcp.tool()
async def get_profile_posts(linkedin_url: str) -> str:
    """Get recent posts of a LinkedIn user by their URL or username."""
    data = await fetch_profile_posts(linkedin_url)
    if not data:
        return "Unable to fetch LinkedIn profile posts data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN PROFILE COMMENTS TOOL ----
async def fetch_profile_comments(linkedin_url: str) -> dict[str, Any] | None:
    # Extract username from LinkedIn URL
    if "/in/" in linkedin_url:
        username = linkedin_url.split("/in/")[1].rstrip("/")
    else:
        username = linkedin_url
    params = {"username": username}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/profile/comments",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn profile comments: {e}")
            return None

@mcp.tool()
async def get_profile_comments(linkedin_url: str) -> str:
    """Get recent comments of a LinkedIn user by their URL or username."""
    data = await fetch_profile_comments(linkedin_url)
    if not data:
        return "Unable to fetch LinkedIn profile comments data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN PROFILE REACTIONS TOOL ----
async def fetch_profile_reactions(linkedin_url: str) -> dict[str, Any] | None:
    # Extract username from LinkedIn URL
    if "/in/" in linkedin_url:
        username = linkedin_url.split("/in/")[1].rstrip("/")
    else:
        username = linkedin_url
    params = {"username": username}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/profile/reactions",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn profile reactions: {e}")
            return None

@mcp.tool()
async def get_profile_reactions(linkedin_url: str) -> str:
    """Get recent reactions of a LinkedIn user by their URL or username."""
    data = await fetch_profile_reactions(linkedin_url)
    if not data:
        return "Unable to fetch LinkedIn profile reactions data."
    return json.dumps(data, indent=2)

# ---- FACEBOOK PROFILE TOOL ----
async def fetch_facebook_profile(profile_url: str) -> dict[str, Any] | None:
    params = {"url": profile_url}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": FACEBOOK_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{FACEBOOK_API_BASE}/profile/details_url",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching Facebook profile: {e}")
            return None

@mcp.tool()
async def get_facebook_profile(profile_url: str) -> str:
    """Fetch Facebook profile data for a given public URL."""
    data = await fetch_facebook_profile(profile_url)
    if not data:
        return "Unable to fetch Facebook profile data."
    return json.dumps(data, indent=2)

# ---- INSTAGRAM PROFILE TOOL ----
async def fetch_instagram_profile(instagram_url_or_username: str) -> dict[str, Any] | None:
    params = {"username_or_url": instagram_url_or_username}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": INSTAGRAM_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{INSTAGRAM_API_BASE}/ig_get_fb_profile_hover.php",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching Instagram profile: {e}")
            return None

@mcp.tool()
async def get_instagram_profile(instagram_url_or_username: str) -> str:
    """Fetch Instagram profile data for a given public username or URL."""
    data = await fetch_instagram_profile(instagram_url_or_username)
    if not data:
        return "Unable to fetch Instagram profile data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN POST COMMENTS TOOL ----
async def fetch_post_comments(post_url: str) -> dict[str, Any] | None:
    params = {"post_url": post_url}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/post/comments",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn post comments: {e}")
            return None

@mcp.tool()
async def get_post_comments(post_url: str) -> str:
    """Get comments, replies, and engagement metrics from LinkedIn posts."""
    data = await fetch_post_comments(post_url)
    if not data:
        return "Unable to fetch LinkedIn post comments data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN POST DETAILS TOOL ----
async def fetch_post_details(post_url: str) -> dict[str, Any] | None:
    params = {"post_url": post_url}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/post/detail",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn post details: {e}")
            return None

@mcp.tool()
async def get_post_details(post_url: str) -> str:
    """Get detailed post and author information for a given LinkedIn post."""
    data = await fetch_post_details(post_url)
    if not data:
        return "Unable to fetch LinkedIn post details data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN POST REACTIONS TOOL ----
async def fetch_post_reactions(post_url: str) -> dict[str, Any] | None:
    params = {"post_url": post_url}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/post/reactions",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn post reactions: {e}")
            return None

@mcp.tool()
async def get_post_reactions(post_url: str) -> str:
    """Get reactions data for a given LinkedIn post."""
    data = await fetch_post_reactions(post_url)
    if not data:
        return "Unable to fetch LinkedIn post reactions data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN POST REPOSTS TOOL ----
async def fetch_post_reposts(post_url: str) -> dict[str, Any] | None:
    params = {"post_url": post_url}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/post/reposts",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn post reposts: {e}")
            return None

@mcp.tool()
async def get_post_reposts(post_url: str) -> str:
    """Get repost data for a given LinkedIn post."""
    data = await fetch_post_reposts(post_url)
    if not data:
        return "Unable to fetch LinkedIn post reposts data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN POSTS SEARCH TOOL ----
async def fetch_posts_search(keyword: str) -> dict[str, Any] | None:
    params = {"keyword": keyword}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/posts/search",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn posts search: {e}")
            return None

@mcp.tool()
async def search_posts(keyword: str) -> str:
    """Get relevant LinkedIn posts for a given keyword."""
    data = await fetch_posts_search(keyword)
    if not data:
        return "Unable to fetch LinkedIn posts search data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN COMPANY POSTS TOOL ----
async def fetch_company_posts(company_identifier: str) -> dict[str, Any] | None:
    params = {"company": company_identifier}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/company/posts",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn company posts: {e}")
            return None

@mcp.tool()
async def get_company_posts(company_identifier: str) -> str:
    """Get posts of a LinkedIn company by name, URL, or URN."""
    data = await fetch_company_posts(company_identifier)
    if not data:
        return "Unable to fetch LinkedIn company posts data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN COMPANIES SEARCH TOOL ----
async def fetch_companies_search(keyword: str) -> dict[str, Any] | None:
    params = {"keyword": keyword}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/companies/search",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn companies search: {e}")
            return None

@mcp.tool()
async def search_companies(keyword: str) -> str:
    """Search for LinkedIn companies using a keyword with optional filters."""
    data = await fetch_companies_search(keyword)
    if not data:
        return "Unable to fetch LinkedIn companies search data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN JOBS SEARCH TOOL ----
async def fetch_jobs_search(keyword: str, location: str = "") -> dict[str, Any] | None:
    params = {"keyword": keyword}
    if location:
        params["location"] = location
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/jobs/search",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn jobs search: {e}")
            return None

@mcp.tool()
async def search_jobs(keyword: str, location: str = "") -> str:
    """Search for jobs on LinkedIn with various filters and parameters."""
    data = await fetch_jobs_search(keyword, location)
    if not data:
        return "Unable to fetch LinkedIn jobs search data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN JOB DETAILS TOOL ----
async def fetch_job_details(job_url: str) -> dict[str, Any] | None:
    params = {"job_url": job_url}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/jobs/detail",
                headers=headers,
                params=params,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn job details: {e}")
            return None

@mcp.tool()
async def get_job_details(job_url: str) -> str:
    """Get detailed information about a specific LinkedIn job posting."""
    data = await fetch_job_details(job_url)
    if not data:
        return "Unable to fetch LinkedIn job details data."
    return json.dumps(data, indent=2)

# ---- LINKEDIN HEALTH CHECK TOOL ----
async def fetch_health_check() -> dict[str, Any] | None:
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/health",
                headers=headers,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching LinkedIn health check: {e}")
            return None

@mcp.tool()
async def check_api_health() -> str:
    """Check if the LinkedIn API is running and healthy."""
    data = await fetch_health_check()
    if not data:
        return "Unable to fetch LinkedIn API health status."
    return json.dumps(data, indent=2)

# ---- WEBSITE SCRAPER TOOL (Google Serper) ----
async def fetch_google_search(query: str, gl: str = "in", num: int = 10, page: int = 1) -> dict[str, Any] | None:
    payload = {
        "q": query,
        "gl": gl,
        "num": num,
        "page": page
    }
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{SERPER_API_BASE}/search",
                headers=headers,
                json=payload,
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching Google search data: {e}")
            return None

@mcp.tool()
async def scrape_website(query: str, gl: str = "in", num: int = 10, page: int = 1) -> str:
    """Fetch search results for a given query using Google Serper API."""
    data = await fetch_google_search(query, gl, num, page)
    if not data:
        return "Unable to fetch Google search data."
    return json.dumps(data, indent=2)

# ---- RUN SERVER ----
if __name__ == "__main__":
    mcp.run(transport="stdio")
