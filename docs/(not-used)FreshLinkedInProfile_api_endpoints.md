# Rapid API LinkedIn API Endpoints Documentation

## Base Information
- **Base rapidapi URL:** `https://fresh-linkedin-profile-data.p.rapidapi.com/`
- **API Provider:** FreshData (FreshData)
- **API Version:** apiversion_63f34a2d-0869-489c-95a4-26f79ccabb47

## Top Endpoints

### 1. Enrich Lead
- **Route:** `/get-personal-profile`
- **Method:** GET
- **Description:** 1 credit per call. Using each extra option will cost another 0.5 credits. Maximum: 3 credits.

### 2. Get Company by URL
- **Route:** `/get-company-by-linkedinurl`
- **Method:** GET
- **Description:** 1 credit per call.

### 3. Get Company by Domain
- **Route:** `/get-company-by-domain`
- **Method:** GET
- **Description:** 1 credit per call.

## Post Data

### 1. Get Profile's Posts
- **Route:** `/get-profile-posts`
- **Method:** GET
- **Description:** 2 credits per call

### 2. Get Post Details
- **Route:** `/get-post-details`
- **Method:** GET
- **Description:** Scrape details of a single post based on its URN.

### 3. Search Posts
- **Route:** `/search-posts`
- **Method:** POST
- **Description:** 2 credits per call.

### 4. Get Post's Reactions
- **Route:** `/get-post-reactions`
- **Method:** GET
- **Description:** 1 credit per call.

### 5. Get Post's Comments
- **Route:** `/get-post-comments`
- **Method:** GET
- **Description:** 1 credit per call.

### 6. Get Company's Posts
- **Route:** `/get-company-posts`
- **Method:** GET
- **Description:** 2 credits per call.

## Lead Search

### 1. Search Leads
- **Route:** `/search-employees`
- **Method:** POST
- **Description:** Find and scrape lead details with advanced filters.

### 2. Lead Search at Scale
- **Route:** `/big-search-employee`
- **Method:** POST
- **Description:** Find and scrape leads at scale

### 3. Search leads V2
- **Route:** `/search-employees-by-sales-nav-url`
- **Method:** POST
- **Description:** Provide search url instead of filters

### 4. Get Search Results
- **Route:** `/get-search-results`
- **Method:** GET
- **Description:** Get search results. Please make sure the search is "done" before calling this endpoint.

### 5. Check Search Status
- **Route:** `/check-search-status`
- **Method:** GET
- **Description:** Get the status of your search using the request_id given in step 1.

## Company Search

### 1. Search Companies
- **Route:** `/search-companies`
- **Method:** POST
- **Description:** Step 1: Use this endpoint to make a search using your criteria. This endpoint will return a "request_id" so that you can check for the search status anytime in step 2. This endpoint will cost you 25 credits per request.

Step 2: Check the search status using the endpoint "Check Company Search Status" (free).

Step 3: Once the search is done, you can start collecting the results by using the endpoint "Get Companies". This endpoint will cost you 1 credit per one company. For example, if your search returns 100 results, it'll cost 100 credits.

### 2. Search Companies by SN URL
- **Route:** `/search-companies-by-sales-nav-url`
- **Method:** POST
- **Description:** Provide URL instead of filters.

### 3. Get Companies
- **Route:** `/get-search-companies-results`
- **Method:** GET
- **Description:** Get search results. Please make sure the search is "done" before calling this endpoint.

### 4. Check Company Search Status
- **Route:** `/check-search-companies-status`
- **Method:** GET
- **Description:** Get the status of your search using the request_id given in step 1.

## Job Search

### 1. Search Jobs
- **Route:** `/search-jobs`
- **Method:** POST
- **Description:** To scrape all results from each search, change the parameter "start" from 0 to 25, 50, etc. until you see less than 25 results returned. 2 credits per call.

### 2. Search Jobs V2
- **Route:** `/search-jobs-v2`
- **Method:** POST
- **Description:** Using a simpler payload. 1 credit per call.

### 3. Get Job Details
- **Route:** `/get-job-details`
- **Method:** GET
- **Description:** Scrape the full job details, including the company basic information. 1 credit per call.

## Other Endpoints

### 1. Get Company by ID
- **Route:** `/get-company-by-id`
- **Method:** GET
- **Description:** 1 credit per call.

### 2. Find Custom Headcount
- **Route:** `/find-custom-headcount`
- **Method:** POST
- **Description:** Discover the count of employees within a specific company who meet designated criteria. 1 credit per call.

### 3. Count Job Openings
- **Route:** `/get-company-jobs-count`
- **Method:** GET
- **Description:** Get the number of job openings a company has posted on LinkedIn. 1 credit per call.

### 4. Google Profiles
- **Route:** `/google-profiles`
- **Method:** POST
- **Description:** **2** credits per call.

### 5. Get Profile PDF CV
- **Route:** `/get-profile-pdf-cv`
- **Method:** GET
- **Description:** **1 credit per call.**

### 6. Get Open to Work Status
- **Route:** `/get-opentowork-status`
- **Method:** GET
- **Description:** **1 credit per call.**

### 7. Get Open Profile Status
- **Route:** `/get-open-profile-status`
- **Method:** GET
- **Description:** **1 credit per call.**

### 8. Get Profile Latest Post Date
- **Route:** `/profile-latest-post-date`
- **Method:** GET
- **Description:** Find out when he/she posted recently.

### 9. Detect Activity Time
- **Route:** `/get-profile-recent-activity-time`
- **Method:** GET
- **Description:** Get the time of the latest profile activity. 2 credits per call.

### 10. Search Decision Makers
- **Route:** `/search-decision-makers`
- **Method:** POST
- **Description:** Search for decision makers of any company.

### 11. Get Company Insights
- **Route:** `/get-company-insights`
- **Method:** GET
- **Description:** 5 credits per call.

### 12. Get Extra Profile Data
- **Route:** `/get-extra-profile-data`
- **Method:** GET
- **Description:** Get more profile's data fields like languages, top skills, certifications, publications, patents, awards

### 13. Get Years of Experience
- **Route:** `/get-year-of-experiences`
- **Method:** GET
- **Description:** Get the total number of years of experience of a profile.

### 14. Get Recommendation Received
- **Route:** `/get-recommendations-received`
- **Method:** GET
- **Description:** Get profile's recommendations (received). **1 credit per call**.

### 15. Get Recommendation Given
- **Route:** `/get-recommendations-given`
- **Method:** GET
- **Description:** Get profile's recommendations (given). **1 credit per call**.

### 16. Search Companies Instantly
- **Route:** `/search-companies-instantly`
- **Method:** POST
- **Description:** Search companies in our cached database of 64 million records (updated annually). Instant results. Cost: 1 credit for 10 companies (searches returning fewer than 10 results still consume 1 credit).

### 17. Search LinkedIn Company Pages via Google
- **Route:** `/google-companies`
- **Method:** POST
- **Description:** Find up to 100 companies that match your criteria via Google. **2** credits per call.

### 18. Search Linkedin School Pages via Google
- **Route:** `/google-schools`
- **Method:** POST
- **Description:** Find up to 100 schools that match your criteria via Google. **2** credits per call.

---

**Total Endpoints:** 32 unique API endpoints for LinkedIn data extraction
**API Groups:** 6 (Top Endpoints, Post Data, Lead Search, Company Search, Job Search, Other Endpoints)
**API Version:** apiversion_63f34a2d-0869-489c-95a4-26f79ccabb47 