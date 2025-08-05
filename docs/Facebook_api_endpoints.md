# Rapid API Facebook API Endpoints Documentation

## Base Information
- **Base rapidapi URL:** `https://facebook-scraper3.p.rapidapi.com/`
- **API Version:** apiversion_13a24a77-7131-45f6-901f-174b14703550

## Search

### 1. Search Locations
- **Route:** `/search/locations`
- **Method:** GET
- **Description:** Search for facebook locations id. If you get strange results, try add country to query and/or try without diacritic

### 2. Search Posts
- **Route:** `/search/posts`
- **Method:** GET
- **Description:** Performs facebook posts search

### 3. Search Places
- **Route:** `/search/places`
- **Method:** GET
- **Description:** Search for fb place

### 4. Search Pages
- **Route:** `/search/pages`
- **Method:** GET
- **Description:** Searches for facebook pages

## Pages

### 1. Page ID
- **Route:** `/page/page_id`
- **Method:** GET
- **Description:** Get page id from url

### 2. Page Events
- **Route:** `/page/events/future`
- **Method:** GET
- **Description:** Get all future events created by page

### 3. Page Future Events
- **Route:** `/page/events/future`
- **Method:** GET
- **Description:** Get all future events created by page

## Events

### 1. Events Details by URL
- **Route:** `/event/details`
- **Method:** GET
- **Description:** Get events details

## Profiles

### 1. Profiles Details by ID
- **Route:** `/profile/details_id`
- **Method:** GET
- **Description:** Get profiles details by id

### 2. Profile Details by URL
- **Route:** `/profile/details_url`
- **Method:** GET
- **Description:** Get profile details by url

### 3. Profile ID
- **Route:** `/profile/profile_id`
- **Method:** GET
- **Description:** Get profile id by url

## Posts and Comments

### 1. Get Post Details
- **Route:** `/post`
- **Method:** GET
- **Description:** Get post details by url or post id. If both are set, post id is used.

### 2. Post Comments
- **Route:** `/post/comments`
- **Method:** GET
- **Description:** Get post comments

### 3. Post Reshares
- **Route:** `/post/share`
- **Method:** GET
- **Description:** Get post reshares

## Groups

### 1. Get Group Details
- **Route:** `/group/details`
- **Method:** GET
- **Description:** Get group summary

### 2. Get Group ID
- **Route:** `/group/id`
- **Method:** GET
- **Description:** Getting group facebook id

## Hashtags

### 1. Search Hashtag
- **Route:** `/search/hashtags`
- **Method:** GET
- **Description:** Search posts with hashtag

---

**Total Endpoints:** 15 unique API endpoints for Facebook data extraction
**API Groups:** 7 (Search, Pages, Events, Profiles, Posts and Comments, Groups, Hashtags)
**API Version:** apiversion_13a24a77-7131-45f6-901f-174b14703550 