from pymongo import MongoClient

from bot.data_sources.external_news_sources.source_types.source_types import News


class MongoDbRepository:
    def __init__(self):
        self._client = None

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        self._client = MongoClient()

    def close(self):
        self._client.close()

    def save_news(self, news: News):
        pass
