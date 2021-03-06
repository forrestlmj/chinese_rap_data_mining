# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Craw163Item(scrapy.Item):
    artist_id = scrapy.Field()
    artist_name = scrapy.Field()


class SingerItem(scrapy.Item):
    name = scrapy.Field()
    artistLink = scrapy.Field()
    isCertificated = scrapy.Field()
    userHomeLink = scrapy.Field()
    timestamp = scrapy.Field()
