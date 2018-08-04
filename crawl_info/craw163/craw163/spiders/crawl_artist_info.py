# TODO 20170916 crawler API for rap artist
# ref: http://moonlib.com/606.html
# TEST artist:eminem,tupac,snoop dog,BIG,nas

import scrapy
class CrawlArtistInfo(scrapy.Spider):
    name = "crawl_artist_info"
    def start_requests(self):
        urls = [
            "https://music.163.com/discover/artist/cat?id=2001&initial=70"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        a = response.text
        print(response)