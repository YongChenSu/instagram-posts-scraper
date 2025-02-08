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


target_info = {"username": "joemanweng", "days_limit":5}
ig_posts_scraper = InstaPeriodScraper()
res = ig_posts_scraper.get_posts(target_info=target_info)
```

### Optional parameters

- **username**: target instagram user 
- **days_limit**: Number of days within which to scrape posts..
## Result Sample

```
{
    'profile': {
        'introduction': ['台灣Youtuber\n⬇️專屬團購連結⬇️'],
        'counts_of_posts': '1392',
        'followers': '581198',
        'followings': '859'
    },
    'account_status': 'public',
    'updated_at': datetime.datetime(2025, 2, 9, 1, 28, 8, 793770, tzinfo=<DstTzInfo 'Asia/Taipei' CST+8:00:00 STD>),
    'data': [
        {
            'type': 'igtv',
            'sum': '《靈能的挑戰》參賽者後台花絮露出👀\n老師們比賽中較勁，但私下娛樂竟是互相算命！\n不知道有沒有先算出冠軍了（吃瓜）\n預祝大家新年快樂~~\n*節目中個人言論不代表本節目立場*\n﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏\n#靈能的挑戰\xa0#Joeman\xa0#東森超視33頻道\n全台第一檔靈能競賽節目\n📺️ 全季觀看平台｜\n🎥 Joeman YT 頻道觀看全季\n🎥 東森超視 33 頻道已播出完畢\n﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋\n#玄學 #易經 #塔羅 #通靈 #占星',
            'sum_pure': '《靈能的挑戰》參賽者後台花絮露出 老師們比賽中較勁，但私下娛樂竟是互相算命！不知道有沒有先算出冠軍了（吃瓜）預祝大家新年快樂~~*節目中個人言論不代表本節目立場*﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏#靈能的挑戰\xa0#Joeman\xa0#東森超視33頻道全台第一檔靈能競賽節目 ️ 全季觀看平台｜ Joeman YT 頻道觀看全季 東森超視 33 頻道已播出完畢﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋﹋#玄學 #易經 #塔羅 #通靈 #占星',
            'shortcode': '6741582137415658464423',
            'time': 1737885600,
            'ftime': '13 days ago',
            'count_like': 2442,
            'count_comment': 6,
            'count_like_pure': '2,442',
            'count_comment_pure': '6',
            'thum': 'https://scontent-fra3-1.cdninstagram.com/v/t51.2885-15/474907887_1129543381888335_8766424988966118915_n.jpg?stp=c0.248.640.640a_dst-jpg_e15_tt6&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_cat=103&_nc_ohc=YPiycXP_teMQ7kNvgF-DLaF&_nc_gid=3e3699c22b4246b98fb450d120d9527f&edm=APU89FABAAAA&ccb=7-5&oh=00_AYAb75YGceozAPWzbq4CQQGd_q_XyfKdjdwcKYak3J-pHA&oe=67AD07FF&_nc_sid=bc0c2c',
            'pic': 'https://scontent-fra3-1.cdninstagram.com/v/t51.2885-15/474907887_1129543381888335_8766424988966118915_n.jpg?stp=dst-jpg_e15_tt6&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_cat=103&_nc_ohc=YPiycXP_teMQ7kNvgF-DLaF&_nc_gid=3e3699c22b4246b98fb450d120d9527f&edm=APU89FABAAAA&ccb=7-5&oh=00_AYA0qczIKFhJEbukWZRRSUvJJ28iqBuhIXZqRB3EEA450Q&oe=67AD07FF&_nc_sid=bc0c2c',
            'pic_p': 'https://sp1.piokok.com/p/pt_6741582137415658464423_0_233bd378e8b9a4f088f6c850099951c7.jpg?u=https%3A%2F%2Fscontent-fra3-1.cdninstagram.com%2Fv%2Ft51.2885-15%2F474907887_1129543381888335_8766424988966118915_n.jpg%3Fstp%3Dc0.248.640.640a_dst-jpg_e15_tt6%26_nc_ht%3Dscontent-fra3-1.cdninstagram.com%26_nc_cat%3D103%26_nc_ohc%3DYPiycXP_teMQ7kNvgF-DLaF%26_nc_gid%3D3e3699c22b4246b98fb450d120d9527f%26edm%3DAPU89FABAAAA%26ccb%3D7-5%26oh%3D00_AYAb75YGceozAPWzbq4CQQGd_q_XyfKdjdwcKYak3J-pHA%26oe%3D67AD07FF%26_nc_sid%3Dbc0c2c',
            'down_pic': 'https://scontent-fra3-1.cdninstagram.com/v/t51.2885-15/474907887_1129543381888335_8766424988966118915_n.jpg?stp=dst-jpg_e15_tt6&_nc_ht=scontent-fra3-1.cdninstagram.com&_nc_cat=103&_nc_ohc=YPiycXP_teMQ7kNvgF-DLaF&_nc_gid=3e3699c22b4246b98fb450d120d9527f&edm=APU89FABAAAA&ccb=7-5&oh=00_AYA0qczIKFhJEbukWZRRSUvJJ28iqBuhIXZqRB3EEA450Q&oe=67AD07FF&_nc_sid=bc0c2c&dl=1',
            'is_video': True,
            'video': 'https://scontent-fra3-1.cdninstagram.com/o1/v/t16/f2/m86/AQNbkAdWefxU8OJ015A7RX0oUxLJS-03KKFEbd2ueAbuWXS5jla4AsgRPhGeuuD9HsvVUz0mG5uKwOTWpYhvCVbbIPtxarY3vAIwG7A.mp4?stp=dst-mp4&efg=eyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uY2xpcHMuYzIuNzIwLmJhc2VsaW5lIn0&_nc_cat=103&vs=427033163733715_1223826287&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9ERDQ1NERCQUU1RkU4RDA5MzA5NzA2Q0IzODgxRUVBM192aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dPcGZUeHgyY1EtV3l3c0VBQjRRdldDeTRZdHFicV9FQUFBRhUCAsgBACgAGAAbABUAACamtPfZ0u%2BTQBUCKAJDMywXQF2QEGJN0vIYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HAA%3D%3D&_nc_rid=3e36937551&ccb=9-4&oh=00_AYANPnQ7Zlk5Z_6wS0OF1Hn3ttS8vsk-0K6OyM9y8xzM6A&oe=67A925DC&_nc_sid=bc0c2c',
            'down_video': 'same_as_above'
        }
    ]
}




## Contributing - Sample

comming soon..

## License - Sample

comming soon..

## Tests - cd to tests folder
coverage run test_crawler.py

coverage html
