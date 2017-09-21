# TODO 20170916 search artist ID by giving artist name
# Full request URI: http://music.163.com/api/artist/albums/166009?id=166009&offset=0&total=true&limit=5
# TEST artist:eminem(32665),tupac,snoop dog,BIG,nas,50cent
import scrapy
from scrapy.utils.response import open_in_browser

class searchArtist(scrapy.Spider):
    name = "search_artist"

    def start_requests(self):
        search_words = {"Eminem", "Tupac", "gai", "马思唯"}
        for search_word in search_words:
            url = "http://music.163.com/api/search/get/"
            data = {"s": search_word, "limit": 1, "type": 100}
            url2 = "http://music.163.com/api/search/get/?s=gai&limit=1&type=100"
            # TODO 20170916 Can not make a post request.In lib requests it works,using Postman get 403 forbidden error.
            yield scrapy.Request(url=url, method="POST", body=str(data),
                                 callback=self.parse, cookies={"appver": "1.5.2"})

    def parse(self, response):
        open_in_browser(response)
        page = response.body
        yield {"content": response}
        print(page)

