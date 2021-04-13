from .source_types import BaseSource, RssSource


class DataSourceSingleDispatch:
    _classes = {
        'rss': RssSource
    }

    @classmethod
    def dispatch(cls, source_name: str) -> BaseSource:
        return cls._classes[source_name]
