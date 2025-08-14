
from pymongo import MongoClient


class MongoDB:
    def __init__(
        self,
        host,
        name_database,
        name_collection,
    ):
        self.client = MongoClient(host)
        self.db = self.client[name_database]
        self.colecao = self.db[name_collection]
