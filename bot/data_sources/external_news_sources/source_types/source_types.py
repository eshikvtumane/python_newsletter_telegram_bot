from dataclasses import dataclass
from typing import Dict, Any

import feedparser


@dataclass
class News:
    identifier: str
    title: str
    link: str
    published_at: str


class BaseSource:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
        self.identifier = None
        self._text = None

        self._generate_identifier()

    def _generate_identifier(self):
        source_name_transform = self.name.replace(' ', '_')
        self.identifier = f'{self.get_class_name()}_{source_name_transform}'

    def __repr__(self):
        return f'<{self.get_class_name()}>: {self.name}>'

    def get_class_name(self):
        return self.__class__.__name__

    def set_text(self, text: str):
        self._text = text

    def get_text(self) -> str:
        return self._text

    def get_news(self) -> News:
        raise NotImplemented


class RssSource(BaseSource):
    def get_news(self) -> News:
        if not self.get_text():
            return []

        try:
            parsed_news = feedparser.parse(url_file_stream_or_string=self.get_text())
        except feedparser.ThingsNobodyCaresAboutButMe as ex:
            return []

        return [News(
            identifier=self.identifier,
            title=news['title'],
            link=news['link'],
            published_at=self._get_published_at(news=news)
        ) for news in parsed_news['entries']]

    def _get_published_at(self, news: Dict[str, Any]) -> str:
        if 'published' in news:
            return news['published']
        elif 'updated' in news:
            return news['updated']

        return ''
