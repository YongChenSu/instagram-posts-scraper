# -*- coding: utf-8 -*-
from src.request import *
from src.parse import *
from src.utils import *
from src.scraper import *
from src.utils.utils import *
from file_operation import *


class ScrapedDataManager(object):
    def __init__(self):
        pass


class InstaPeriodScraper(object):
    def __init__(self) -> None:
        self.pixwox_request = PixwoxRequest()
        self.parser=Parser()
        self.api_parser=ApiParser()
        self.scraper=Scraper( 
            pixwox_request=self.pixwox_request, 
            parser=self.parser, 
            api_parser=self.api_parser
        )

    def check_account_is_public(self):
        init_response = self.pixwox_request.send_requests(url=self.scraper.init_url)
        self.profile_soup = self.parser.get_soup(response=init_response)
        self.userid = self.parser.get_userid(profile_soup=self.profile_soup)
        self.account_status = get_account_status(userid=self.userid, profile_soup=self.profile_soup)
        return self.account_status == "public"
    
    def get_profile(self):
        self.followings = self.parser.get_followings(self.profile_soup)
        self.followers = self.parser.get_followers(self.profile_soup)
        self.counts_of_posts = self.parser.get_counts_of_posts(self.profile_soup)
        try:
            self.introduction = self.parser.get_introduction(self.profile_soup)
        except:
            self.introduction = None
        
        self.profile_info = {
            "introduction": self.introduction,
            "counts_of_posts": self.counts_of_posts,
            "followers": self.followers,
            "followings": self.followings,
        }

    def get_init_api_data(self):
        init_api_data = self.scraper.get_init_api_data(userid=self.userid)
        return init_api_data
    
    def get_next_api_data(self, next_maxid:str, next_:str,username:str):
        next_api_data = self.scraper.get_next_api_data(userid=self.userid, next_maxid=next_maxid, next_=next_, username=username)
        return next_api_data

    def get_private_account_res(self):
        res = {
            "profile":{
                "userid":self.userid,
                "username":self.target_info["username"],
                "followers":self.followers,
                "followings":self.followings,
                "counts_of_posts":self.counts_of_posts,
                "introduction":self.introduction
                },
            "account_status":self.account_status,
            "updated_at": get_current_time(timezone="Asia/Taipei"),
            "data":[]
        }
        return res

    def get_missing_account_res(self):
        res = {
            "profile":{
                "userid":None,
                "username":self.target_info["username"],
                "followers":None,
                "followings":None,
                "counts_of_posts":None,
                "introduction":None
                },
            "account_status":self.account_status,
            "updated_at": get_current_time(timezone="Asia/Taipei"),
            "data":[]
        }
        return res

    def get_public_account_res(self, scraped_posts, init_api_data):
        res = {
            "profile": self.profile_info,
            "account_status":self.account_status,
            "updated_at": get_current_time(timezone="Asia/Taipei"),
            "data":scraped_posts}
        return res

    # @timeout(300)
    def get_period_data(self, days_limit:int, init_maxid:str, init_api_data, username):
        scraped_posts_res = init_api_data["posts"]["items"]
        next_ = init_api_data["posts"]["next"]
        next_maxid = init_maxid
        for rounds in range(days_limit):
            # Scraped next rounds data
            next_api_data = self.get_next_api_data(next_maxid=next_maxid, next_=next_, username=username)
            scraped_posts = next_api_data["posts"]
            scraped_items = scraped_posts["items"]
            scraped_posts_res += scraped_items
            
            # if get all posts or get target period posts
            if has_all_data_been_collected(scraped_items=scraped_posts_res, counts_of_posts=self.counts_of_posts) or is_date_exceed_half_year(scraped_items=scraped_items,days_limit=days_limit):
                return scraped_posts_res
            
            elif next_api_data["posts"]["has_next"]: # if there are posts can scrape
                next_maxid = scraped_posts["maxid"]
                next_ = scraped_posts["next"]
                continue
            else:
                return scraped_posts_res
        return scraped_posts_res
    
    def get_posts(self, target_info:dict):
        self.target_info = target_info
        self.username = self.target_info["username"]
        username = self.target_info["username"]
        self.scraper.set_username(username)
        days_limit = target_info["days_limit"]
        if not self.check_account_is_public():
            print("This is private account")
            if self.account_status == "private":
                self.get_profile()
                res = self.get_private_account_res()
                return res
            elif self.account_status == "missing":
                res = self.get_missing_account_res()
                return res
        
        if self.check_account_is_public():
            init_api_data = self.get_init_api_data() # 帳號資訊 & 上方頁面內容
            self.get_profile()
            print(f"This is public account")
            # can scrape next round's posts
            if init_api_data["posts"]["has_next"] != False:
                maxid = init_api_data["posts"]["maxid"]
                period_posts = self.get_period_data(
                    init_maxid=maxid,
                    days_limit=days_limit,
                    init_api_data=init_api_data,
                    username=username
                    )

                # return period_posts
                res = self.get_public_account_res(
                    scraped_posts=period_posts, 
                    init_api_data=init_api_data
                    )
                return res
            # # no more posts
            elif init_api_data["posts"]["has_next"] == False: # (表示該帳號貼文數<=12, 無法繼續往下找)
                res = self.get_public_account_res(scraped_posts=init_api_data["posts"]["items"], init_api_data=init_api_data)
                return res
