# -*- coding: utf-8 -*-
#%%
from instagram_posts_scraper.instagram_posts_scraper import InstaPeriodScraper

target_info = {"username": "mapleshadow18", "days_limit":5}
ig_posts_scraper = InstaPeriodScraper()
res = ig_posts_scraper.get_posts(target_info=target_info)
res
# %%
