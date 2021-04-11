import pytest

from bot.data_sources.source_types import DataSourceList
from bot.data_sources.source_types.source_types import BaseSource
from bot.data_sources.sources import SOURCES_INFO
from bot.exceptions import BotValidationSourceIdentifiersError


class TestDataSourceList:
    def test_create_from_dict(self):
        data_source_objs = DataSourceList.from_dict(sources=SOURCES_INFO)

        assert all(isinstance(data_source, BaseSource) for data_source in data_source_objs) is True,\
            u"Wrong source class type."

    def test_validate_unique_identifiers_success(self):
        data_source_objs = DataSourceList.from_dict(sources=SOURCES_INFO)

        data_source_objs.validate()

    def test_validate_unique_identifiers_error(self):
        data_source_objs = DataSourceList.from_dict(sources=SOURCES_INFO)
        data_source_objs.extend(data_source_objs[:2])
        identifiers = [data_source_obj.identifier for data_source_obj in data_source_objs[:2]]
        union_identifiers = ', '.join(identifiers)

        data_source_objs.validate()

        with pytest.raises(BotValidationSourceIdentifiersError, match=union_identifiers):
            raise BotValidationSourceIdentifiersError(identifiers=identifiers)
