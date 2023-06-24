# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


import os
import json
from datetime import datetime


class ArabicfiScraperPipeline:
    def __init__(self):
        now = datetime.now()
        self.file_name = "data/words_" + now.strftime("%Y-%m-%d_%Hh%Mm%Ss") + ".jsonl"
        # db_name = "products.db"
        if os.path.isfile("data"):
            os.remove("data")
        if not os.path.isdir("data"):
            os.makedirs("data")
        if os.path.isfile(self.file_name):
            os.remove(self.file_name)

    def open_spider(self, spider):
        self.file = open(self.file_name, "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
