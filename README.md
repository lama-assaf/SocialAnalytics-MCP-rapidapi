<h1 align="center">Social Media Scraper - Custom MCP Server</h1>

A comprehensive Model Context Protocol (MCP) server that provides social media scraping capabilities for LinkedIn, Facebook, Instagram, and Google search functionality.

## What is MCP?

**[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)** is an open standard that enables AI assistants to securely connect with external data sources and tools. MCP servers act as bridges between AI models and various services, allowing for enhanced capabilities like real-time data access, API integrations, and custom tool execution.

## Features
This server exposes the following tools for an AI assistant to use:
- **LinkedIn Profile Scraping**: Extract personal and company profile data
- **Facebook Profile Scraping**: Fetch public profile information
- **Instagram Profile Scraping**: Get profile data and basic information
- **Google Search**: Perform web searches using Google Serper API

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

### Example Usage

```
Please scrape this LinkedIn profile: https://linkedin.com/in/example-profile
```

```
Get company information for: https://linkedin.com/company/example-company
```

## Troubleshooting

If the MCP tools don't appear in Claude Desktop:

### Step 1: End Claude Processes
- Windows: Open Task Manager (Ctrl+Shift+Esc)
- Mac: Open Activity Monitor
- End all Claude-related processes

### Step 2: Reinstall the Server
```bash
uv run mcp install main.py
```

### Step 3: Restart Claude Desktop

Paste the URLs of required platform and ask the AI to provide information of the mentioned URLs.

### Testing with MCP Inspector

Alternatively, you can test it with the MCP Inspector:

```bash
uv run mcp dev main.py
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

## Response Format

All tools return JSON-formatted strings containing the scraped data. Example response structure:

```json
{
  "success": true,
  "data": {
    "profile": {
      "name": "John Doe",
      "title": "Software Engineer",
      "location": "San Francisco, CA",
      "bio": "Passionate about technology..."
    }
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```
But using these tools via Claudes makes it readable.

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
