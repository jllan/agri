# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient



class CropPipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client['agri_resource']
        self.collection = db['agri_qa']

    def process_item(self, item, spider):
        self.collection.update({'url': item['url']}, item, True)
        return item