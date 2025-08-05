# Rapid API LinkedIn Scraper API Endpoints Documentation

## Base Information
- **Base rapidapi URL:** `https://linkedin-scraper-api-real-time-fast-affordable.p.rapidapi.com/`
- **API Version:** apiversion_ee328436-3345-4014-af10-b5ed5b9d0a19

## Profiles API

### 1. Profile Details
- **Route:** `/profile/detail`
- **Method:** GET
- **Description:** Get detailed profile information for a LinkedIn user by their username
- **Group:** Profiles API

### 2. Profile Posts
- **Route:** `/profile/posts`
- **Method:** GET
- **Description:** Get the recent posts of a LinkedIn user by their username
- **Group:** Profiles API

### 3. Profile Comments
- **Route:** `/profile/comments`
- **Method:** GET
- **Description:** Get the recent comments of a LinkedIn user by their username
- **Group:** Profiles API

### 4. Profile Reactions
- **Route:** `/profile/reactions`
- **Method:** GET
- **Description:** Get the recent comments of a LinkedIn user by their username
- **Group:** Profiles API

## Posts API

### 1. Post Comments, Replies & Stats
- **Route:** `/post/comments`
- **Method:** GET
- **Description:** Get comments, replies, and engagement metrics from LinkedIn posts including author details, reaction counts, timestamps, and nested replies
- **Group:** Posts API

### 2. Post Details
- **Route:** `/post/detail`
- **Method:** GET
- **Description:** Get detailed post and author information for a given post
- **Group:** Posts API

### 3. Post Reactions
- **Route:** `/post/reactions`
- **Method:** GET
- **Description:** Get reactions data for a given linkedin post
- **Group:** Posts API

### 4. Post Reshares
- **Route:** `/post/reposts`
- **Method:** GET
- **Description:** Get repost data for a given post
- **Group:** Posts API

### 5. Posts Search
- **Route:** `/posts/search`
- **Method:** GET
- **Description:** Get relevant posts for a given keyword
- **Group:** Posts API

## Companies API

### 1. Company Details
- **Route:** `/companies/detail`
- **Method:** GET
- **Description:** Get detailed information about a company using its name, LinkedIn URL or URN.

**Examples:**
- Using company name: youtube
- Using LinkedIn URL: https://www.linkedin.com/company/youtube/
- Using URN: 1035
- **Group:** Companies API

### 2. Company Posts
- **Route:** `/company/posts`
- **Method:** GET
- **Description:** Get posts of company

**Examples:**
- Using company name: google
- Using LinkedIn URL: https://www.linkedin.com/company/google/
- Using URN: 1035
- **Group:** Companies API

### 3. Companies Search
- **Route:** `/companies/search`
- **Method:** GET
- **Description:** Search for LinkedIn companies using a keyword with optional filters
- **Group:** Companies API

## Jobs API

### 1. Search Jobs
- **Route:** `/jobs/search`
- **Method:** GET
- **Description:** Search for jobs on LinkedIn with various filters and parameters
- **Group:** Jobs API

### 2. Job Details
- **Route:** `/jobs/detail`
- **Method:** GET
- **Description:** Get detailed information about a specific job posting
- **Group:** Jobs API

## System API

### 1. Health Check
- **Route:** `/health`
- **Method:** GET
- **Description:** Check if the API is running
- **Group:** System API

---

**Total Endpoints:** 13 unique API endpoints for LinkedIn data extraction
**API Groups:** 5 (Profiles API, Posts API, Companies API, Jobs API, System API)
**API Version:** apiversion_ee328436-3345-4014-af10-b5ed5b9d0a19

## API Groups Summary

1. **Profiles API** - User profile data and activity
2. **Posts API** - Post content, engagement, and search functionality
3. **Companies API** - Company information and posts
4. **Jobs API** - Job search and details
5. **System API** - API health and status monitoring

## Key Features

- **Real-time Data:** Fast and affordable LinkedIn data extraction
- **Comprehensive Coverage:** Profile details, posts, comments, reactions, companies, and jobs
- **Flexible Search:** Multiple search options with various filters
- **Engagement Metrics:** Detailed analytics including reactions, comments, and reposts
- **Multiple Input Formats:** Support for usernames, URLs, and URNs
- **Nested Data:** Comments with replies and author details
- **Company Intelligence:** Company posts and detailed information
- **Job Market Data:** Job search and detailed job postings 