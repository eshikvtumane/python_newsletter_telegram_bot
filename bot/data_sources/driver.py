from .sources import SOURCES_INFO


class DataSourcesDriver:
    def __init__(self):
        self._sources = []
        self._get_sources()

    def _get_sources(self):
        SOURCES_INFO
