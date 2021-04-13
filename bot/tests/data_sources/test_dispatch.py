import pytest

from bot.data_sources.external_news_sources.source_types.dispatch import DataSourceSingleDispatch
from bot.data_sources.external_news_sources.source_types.source_types import RssSource


class TestDispatch:
    @pytest.mark.parametrize(
        ('source_type_name', 'source_type_class'),
        (
            ('rss', RssSource),
        )
    )
    def test_dispatch(self, source_type_name, source_type_class):
        class_obj = DataSourceSingleDispatch.dispatch(source_name=source_type_name)

        assert class_obj == source_type_class, "Wrong class object."
