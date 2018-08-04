# TODO 20170916 search artist ID by giving artist name
# ref:https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/
# Full request URI: http://music.163.com/api/artist/albums/166009?id=166009&offset=0&total=true&limit=5
# TEST artist:eminem(32665),tupac,snoop doG,nas,50cent
import scrapy
import json
from scrapy.utils.response import open_in_browser
from craw163.items import Craw163Item

class searchArtist(scrapy.Spider):
    name = "search_artist"

    def start_requests(self):
        # "Eminem", "Tupac", "gai", "马思唯",
        # search_words = {"JonyJ ","PGone","gai","法老","vava","TT","百万","YZ"}

        search_words = {"徐真真"}
        # search_words = {"Eminem"}

        for search_word in search_words:
            url = "http://music.163.com/api/search/get/"
            data = {"s": search_word, "limit": "1", "type": "100"}
            url2 = "http://music.163.com/api/search/get/?s=gai&limit=1&type=100"
            # TODOdone 20170922 Find out the relationship between Request Object and Response,how yield work.
            # yield scrapy.Request(url=url, method="POST", body=str(data),
            #                      callback=self.parse, cookies={"appver": "1.5.2"})
            # TODO why this work??
            yield scrapy.FormRequest(url=url, formdata=data)

    def parse(self, response):
        # open_in_browser(response)

        # print(response.encoding)
        # TODO why this work??ref:https://stackoverflow.com/questions/9181214/scrapy-text-
        # python 2.x:
        # unicode(response.body.decode(response.encoding)).encode('utf-8')
        # python 3.x:
        page = str((response.body.decode(response.encoding)).encode('utf-8'), 'utf-8')
        # print(page)
        page_dict = json.loads(page)
        # print(type(page_dict))
        # print(page_dict)
        item = Craw163Item()
        # TODO 20170928 这里后续还会增加更多的信息，比如中文名，昵称等
        item['artist_id'] = page_dict['result']['artists'][0]['id']
        item['artist_name'] = page_dict['result']['artists'][0]['name']
        yield item
        # yield {"content": page}

