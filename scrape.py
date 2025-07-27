print("🚀 Starting scrape.py...")

from instagram_posts_scraper.instagram_posts_scraper import InstaPeriodScraper

target_info = {"username": "mapleshadow18", "days_limit": 60}
ig_posts_scraper = InstaPeriodScraper()
res = ig_posts_scraper.get_posts(target_info=target_info)

for post in res:  # <- 改這裡，把 posts 改成 res
    print(post)
