import pymongo
from pymongo.results import InsertOneResult


class MongoPipeline:
    collection_name = "scrapy_items"

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://root:password@mongo")
        self.mongo_db = self.client["food"]

    def process_item(self, item) -> InsertOneResult:
        return self.mongo_db[self.collection_name].insert_one(item)

    def get_foods(self, limit):
        try:
            food = list(self.mongo_db[self.collection_name].find({}, {'_id': 0}).limit(limit))
            return food
        except Exception as e:
            print(f"Error occurred while fetching foods from the database: {str(e)}")
            return None

    def get_food(self, barcode: str):
        try:
            code_data = self.mongo_db[self.collection_name].find_one({'barcode': barcode}, {'_id': 0})
            return code_data
        except Exception as e:
            print(f"Error occurred while fetching data from the database: {str(e)}")
            return None

