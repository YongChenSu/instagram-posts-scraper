# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python library for scraping Instagram posts data. The scraper extracts public Instagram user data including profile information, post content, likes, comments, and timestamps within specified date ranges.

## Development Commands

**Installation:**
```bash
pip install -r requirements.txt
```

**Package Installation (for distribution):**
```bash
pip install instagram-posts-scraper
```

**Running the example:**
```bash
python instagram_posts_scraper/example.py
```

**Building/Testing:**
- This project uses setup.py for packaging
- Run tests by executing the example script
- No formal test suite is currently configured

## Architecture

### Core Components

**Main Scraper (`InstaPeriodScraper`)**: Primary interface class that orchestrates the scraping process. Located in `instagram_posts_scraper.py:16-286`.

**Request Handler (`PixwoxRequest`)**: Manages HTTP requests with cloudscraper integration and Cloudflare bypass capabilities. Uses seleniumbase for dynamic content handling.

**HTML Parser (`Parser`)**: Extracts data from HTML responses using BeautifulSoup. Handles profile information, post content, and pagination metadata.

**API Parser (`ApiParser`)**: Processes JSON API responses for pagination data.

**Scraper Orchestrator (`Scraper`)**: Coordinates between request handlers and parsers for API calls.

### Key Data Flow

1. **Account Validation**: Check if target account is public/private/missing
2. **Profile Extraction**: Extract follower count, post count, and bio information  
3. **Initial Data Fetch**: Get first batch of posts from profile page
4. **Pagination Loop**: Use API endpoints to fetch additional posts with retry logic
5. **Data Aggregation**: Combine and deduplicate results

### Anti-Detection Strategy

The scraper implements several techniques to avoid blocking:
- Uses cloudscraper for basic Cloudflare bypass
- Falls back to seleniumbase with undetected-chrome for complex challenges  
- Caches valid headers/cookies in `auth_data/` directory
- Implements progressive retry delays and timeout handling

### URL Patterns

- Profile pages: `https://www.picnob.com/zh-hant/profile/{username}`
- API endpoints: `https://www.piokok.com/api/posts` with pagination parameters
- Fallback service: `https://www.pixnoy.com/profile/{username}` for header generation

## Important Implementation Details

**Cloudflare Handling**: The `get_valid_headers_cookies()` function in `utils/utils.py:80-130` automatically detects when cached credentials are invalid and re-generates them using selenium.

**Pagination Logic**: The `get_period_data()` method implements robust pagination with deduplication using post shortcodes and multiple termination conditions.

**Error Recovery**: Retry logic with exponential backoff is implemented throughout the scraping pipeline to handle temporary failures.

**Date Filtering**: Posts are filtered by publication date to respect the `days_limit` parameter, preventing unnecessary over-scraping.