import asyncio
from typing import Union, Generator

from aiohttp import client_exceptions, ClientSession

from .source_types import DataSourceList
from .source_types.source_types import News
from .sources import SOURCES_INFO


class DataSourcesDriver:
    _SOURCES_INFO = SOURCES_INFO

    def __init__(self):
        self._sources = []
        self._get_sources()

    def _get_sources(self):
        self._sources = DataSourceList.from_dict(sources=self._SOURCES_INFO)

    def get_all_news(self) -> Generator[None, None, News]:
        event_loop = asyncio.get_event_loop()
        event_loop.run_until_complete(self._async_download_news_by_urls(loop=event_loop))
        event_loop.close()

        for source in self._sources:
            for news in source.get_news():
                yield news

    async def _async_download_news_by_urls(self, loop):
        for source in self._sources:
            async with ClientSession(loop=loop) as session:
                text = await self._async_fetch_news_from_url(session=session, url=source.url)
                source.set_text(text=text)

    async def _async_fetch_news_from_url(self, session: ClientSession, url: str) -> Union[str, None]:
        try:
            async with session.get(url=url) as response:
                if response.status == 200:
                    return await response.text()
                return None
        except client_exceptions.ClientConnectorError:
            return None
