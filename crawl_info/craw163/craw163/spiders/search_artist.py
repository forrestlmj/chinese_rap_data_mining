# TODO 20170916 search artist ID by giving artist name
# Full request URI: http://music.163.com/api/artist/albums/166009?id=166009&offset=0&total=true&limit=5
# TEST artist:eminem(32665),tupac,snoop doG,nas,50cent
import scrapy
from scrapy.utils.response import open_in_browser

class searchArtist(scrapy.Spider):
    name = "search_artist"

    def start_requests(self):
        search_words = {"Eminem", "Tupac", "gai", "马思唯"}
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
        open_in_browser(response)
        print(response.encoding)
        # TODO why this work??ref:https://stackoverflow.com/questions/9181214/scrapy-text-
        # python 2.x:
        # unicode(response.body.decode(response.encoding)).encode('utf-8')
        # python 3.x:
        page = str((response.body.decode(response.encoding)).encode('utf-8'), 'utf-8')
        # print(page)
        yield {"content": page}

