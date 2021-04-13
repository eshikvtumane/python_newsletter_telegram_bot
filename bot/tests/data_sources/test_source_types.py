from dataclasses import dataclass

import pytest

from bot.data_sources.external_news_sources.source_types.source_types import RssSource, BaseSource


@dataclass
class SourceTypeParameter:
    type_instance: BaseSource
    name: str
    url: str

    def get_object(self) -> BaseSource:
        return self.type_instance(name='rss_source', url='http://example.com')


SOURCES_TYPE_PARAMETERS = (
    ('source_type_parameter',),
    (
        (SourceTypeParameter(type_instance=RssSource, name='rss_source', url='http://example.com'),),
    ),
)


class TestSourceTypes:
    @pytest.mark.parametrize(*SOURCES_TYPE_PARAMETERS)
    def test_create_type(self, source_type_parameter: SourceTypeParameter):
        type_obj = source_type_parameter.get_object()

        assert type_obj.name == source_type_parameter.name, "Wrong type source name."
        assert type_obj.url == source_type_parameter.url, "Wrong type source url."
        assert type_obj.identifier is not None, "Identifier shouldn't is None."

    @pytest.mark.parametrize(*SOURCES_TYPE_PARAMETERS)
    def test_check_identifier(self, source_type_parameter: SourceTypeParameter):
        type_obj = source_type_parameter.get_object()
        source_name_transform = source_type_parameter.name.replace(' ', ', ')

        expected_identifier = f'{type_obj.__class__.__name__}_{source_name_transform}'

        assert type_obj.identifier == expected_identifier, "Wrong identifier."

    @pytest.mark.parametrize(*SOURCES_TYPE_PARAMETERS)
    def test_get_class_name(self, source_type_parameter: SourceTypeParameter):
        type_obj = source_type_parameter.get_object()
        class_name = f'{type_obj.__class__.__name__}'

        assert type_obj.get_class_name() == class_name, "Wrong class name."
