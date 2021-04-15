from bot.data_sources.database.repository import MongoDbRepository
from bot.data_sources.external_news_sources.driver import DataSourcesDriver


class SynchronizationNews:
    NewsSourceDriver = DataSourcesDriver
    DatabaseDriver = MongoDbRepository

    def run(self):
        news_source_driver = self.NewsSourceDriver()

        for news in news_source_driver.get_all_news():

