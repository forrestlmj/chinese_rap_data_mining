# TODO 20170916 crawler API for rap artist
# ref: http://moonlib.com/606.html
# TEST artist:eminem,tupac,snoop dog,BIG,nas

import scrapy
from datetime import datetime
from ..items import SingerItem
class CrawlArtistInfo(scrapy.Spider):
    name = "crawl_artist_info"
    def start_requests(self):
        for i in range(76, 76+1):
            yield scrapy.Request(url="https://music.163.com/discover/artist/cat?id=2001&initial={0}".format(str(i)))
    def parse(self, response):

        a = response.text
        # for i in response.selector.xpath('//a[@class = "'"msk"'"]').extract():
        #     # singerItem = SingerItem()
        #     # singerItem['name'] =
        #     # singerItem['artistLink'] =
        #     # singerItem['isCertificated'] =
        #     # singerItem['userHomeLink'] =
        #     # singerItem['timestamp'] = datetime.now().strftime("%Y%m%d %H:%M:%S")
        #     print(i)
        # href_list = response.selector.xpath('//a[@class = "'"nm nm-icn f-thide s-fc0"'"]/@href').extract()
        # name_list = response.selector.xpath('//a[@class = "'"nm nm-icn f-thide s-fc0"'"]/text()').extract()
        # enumerate
        links =response.selector.xpath('//a[@class = "'"nm nm-icn f-thide s-fc0"'"]')
        for link in links:
            singerItem = SingerItem()
            try:

                singerItem['name'] = link.xpath('text()').extract_first()
                singerItem['artistLink'] = link.xpath('@href').extract_first()
                singerItem['isCertificated'] = None
                singerItem['userHomeLink'] = None
            except Exception as e:
                print(e)
            singerItem['timestamp'] = datetime.now().strftime("%Y%m%d %H:%M:%S")
            yield singerItem

