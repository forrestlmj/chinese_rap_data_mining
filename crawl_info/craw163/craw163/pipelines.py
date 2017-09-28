# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class Craw163Pipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            a = dict(item)
            log.msg(type(a), level=log.DEBUG, spider=spider)
            log.msg(a, level=log.DEBUG, spider=spider)

            # self.collection.insert(dict(item))

            self.collection.update({"artist_id": a['artist_id']}, a, upsert=True)
            log.msg("Artist added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item
