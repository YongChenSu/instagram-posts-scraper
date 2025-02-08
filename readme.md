# Instagram Posts Scraper

InstagramPostsScraper is a Python library for collect instagram users' data.

The data obtained by web crawlers is not real-time data, but rather data from a specific point in time on the same day.


## Requirements
```bash
beautifulsoup4==4.13.3
cloudscraper==1.2.71
pandas==2.2.3
pytz==2025.1
```

## Installation

To install the latest release from PyPI:

```sh
pip install instagram-posts-scraper
```

## Usage - Sample

```python
from instagram_posts_scraper import InstaPeriodScraper


target_info = {"username": "kaicenat", "days_limit":60}
ig_posts_scraper = InstaPeriodScraper()
res = ig_posts_scraper.get_posts(target_info=target_info)
```

### Optional parameters

- **username**: target instagram user 
- **days_limit**: Number of days within which to scrape posts..

## Sample(Usage & Result) - KaiCenat
![image](https://github.com/FaustRen/instagram-posts-scraper/blob/main/usage.png)

![image](https://github.com/FaustRen/instagram-posts-scraper/blob/main/scraped_posts.png)