# Rapid API Instagram API Endpoints Documentation

## Base Information
- **Base rapidapi URL::**  `https://instagram-scraper-stable-api.p.rapidapi.com/
- **Rate Limit::**  50 requests per minute

## Post & Media Data

### 1. Detailed Media Data v2 (with play_count)
- **Route:** `/get_media_data_v2.php`
- **Method:** GET
- **Description:** Endpoint to extract detailed data for an IG post/reel with fb_play_count, ig_play_count, comments count, etc. Use `media_code` or `media_id` to get detailed data.

### 2. Get Post Likers V2 (with pagination_token)
- **Route:** `/get_post_likers.php`
- **Method:** GET
- **Description:** API to extract the list of users who liked a particular post.

### 3. GET Post Title/Description
- **Route:** `/get_reel_title.php`
- **Method:** GET
- **Description:** Endpoint to get title and description of any post

### 4. Detailed Post Data
- **Route:** `/get_media_data.php`
- **Method:** GET
- **Description:** Endpoint to extract detailed data for an IG post including play_count, likes, comments count, etc.

### 5. Get Reel Title/Description
- **Route:** `/get_reel_title.php`
- **Method:** GET
- **Description:** Endpoint to extract title and description of any IG reel

### 6. Detailed Reel Data
- **Route:** `/get_media_data.php`
- **Method:** GET
- **Description:** Endpoint to extract detailed data for an IG reel including play_count, likes, comments count, etc.

### 7. Get Post Comments
- **Route:** `/get_post_comments.php`
- **Method:** GET
- **Description:** API to extract post comments with pagination

### 8. Get Post/Media Comment Replies
- **Route:** `/get_post_child_comments.php`
- **Method:** GET
- **Description:** API to extract media comment replies

### 9. Get Media Code or ID
- **Route:** `/media_data_id.php`
- **Method:** GET
- **Description:** Endpoint to get: 1. Media Code by ID 2. Media ID by Code. It also includes the final post/media URL.

## User Profile Data

### 1. User Bio Links
- **Route:** `/ig_get_fb_profile.php`
- **Method:** POST
- **Description:** API to get links from the bio of any IG user

### 2. User Stories
- **Route:** `/get_ig_user_stories.php`
- **Method:** POST
- **Description:** Endpoint to get user's latest stories with images and video links

### 3. Are Stories published
- **Route:** `/ig_get_fb_profile.php`
- **Method:** POST
- **Description:** Endpoint to check if a user has stories published or not.

### 4. Basic User + Posts
- **Route:** `/ig_get_fb_profile_hover.php`
- **Method:** GET
- **Description:** Returns basic Instagram account data and latest three posts for any username including number of followers/followings, Media count, HD profile pic, etc

### 5. Account Data
- **Route:** `/ig_get_fb_profile.php`
- **Method:** POST
- **Description:** Returns Instagram account data for any username including number of followers/followings, bio, HD profile pic, etc

### 6. Account Data V2
- **Route:** `/ig_get_fb_profile_v3.php`
- **Method:** POST
- **Description:** Returns Instagram account data for any username including public email/phone, no. of followers/followings, bio, HD profile pic, etc

### 7. User About
- **Route:** `/get_ig_user_about.php`
- **Method:** GET
- **Description:** Get details about a user including "Date Joined", "Verified on Date", "Creation Account", etc.

### 8. User Similar Accounts
- **Route:** `/get_ig_similar_accounts.php`
- **Method:** GET
- **Description:** Get a list of similar users for an IG profile.

### 9. Followers List v2 (with Verified accounts)
- **Route:** `/get_ig_user_followers_v2.php`
- **Method:** POST
- **Description:** Get the list of followers (upto 50 in one request) of any IG user including verified users.

### 10. Followers List
- **Route:** `/get_ig_user_followers.php`
- **Method:** POST
- **Description:** Get the list of followers of any IG user

### 11. Following List v2
- **Route:** `/get_ig_user_followers_v2.php`
- **Method:** POST
- **Description:** Get the list of followings (upto 50 in one request) of any IG user including verified users.

### 12. Following List
- **Route:** `/get_ig_user_followers.php`
- **Method:** POST
- **Description:** Get the list of followings for any IG user

### 13. User Posts
- **Route:** `/get_ig_user_posts.php`
- **Method:** POST
- **Description:** Get user posts with thumbnail and video URLs in multiple dimensions.

### 14. User Reels
- **Route:** `/get_ig_user_reels.php`
- **Method:** POST
- **Description:** Get latest reels of any Instagram user with their video links, images links, comment_count, like_count, like_and_view_counts_disabled, play_count, etc

### 15. User Highlights
- **Route:** `/get_ig_user_highlights.php`
- **Method:** POST
- **Description:** Endpoint to get a list of user highlights

### 16. User Highlight Stories
- **Route:** `/get_highlights_stories.php`
- **Method:** POST
- **Description:** Endpoint to get a list of user stories for a particular highlight using the highlight_id

### 17. User Tagged Posts
- **Route:** `/get_ig_user_tagged_posts.php`
- **Method:** POST
- **Description:** Get a list of user's tagged posts with carousal, images, video links, like_count, comment_count, view_count, etc

## Search & Discovery

### 1. Search (Users + Hashtags)
- **Route:** `/search_ig.php`
- **Method:** POST
- **Description:** Search Instagram for any hashtag, place or a user

### 2. Posts & Reels V2 (with pagination)
- **Route:** `/search_hashtag.php`
- **Method:** GET
- **Description:** Endpoint to extract posts and reels by searching for any hashtag

---

**Total Endpoints:** 28 unique API endpoints for Instagram data extraction
**API Version:** apiversion_c83204b3-472b-47b9-985e-d0d9747f9009