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
LINKEDIN_HOST = "fresh-linkedin-profile-data.p.rapidapi.com"
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
    params = {"linkedin_url": linkedin_url}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/get-linkedin-profile",
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
    params = {"linkedin_url": linkedin_url}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": LINKEDIN_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{LINKEDIN_API_BASE}/get-company-by-linkedinurl",
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
