# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from repository.handler_db import MongoPipeline


# useful for handling different item types with a single interface


class ScrapingPipeline:
    def __init__(self):
        self.db_pipeline = MongoPipeline()

    def process_item(self, item, spider) -> None:
        self.db_pipeline.process_item(item)
