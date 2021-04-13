from typing import Dict, List, Any

from bot.data_sources.external_news_sources.source_types.dispatch import DataSourceSingleDispatch
from bot.exceptions import BotValidationSourceIdentifiersError


class DataSourceList(list):
    _dispatch_method_for_type_source = DataSourceSingleDispatch.dispatch

    @classmethod
    def from_dict(cls, sources: Dict[str, List[Dict[str, Any]]]):
        data_source_list = cls()

        for type_name, type_items in sources.items():
            type_source_class = cls._dispatch_method_for_type_source(source_name=type_name)

            for item in type_items:
                data_source_list.append(type_source_class(name=item['name'], url=item['url']))

        return data_source_list

    def validate(self):
        validate_method_names = filter(lambda name: '_validate_' in name, dir(self))

        for method_name in validate_method_names:
            getattr(self, method_name)()

    def _validate_unique_identifiers(self):
        identifiers = set()
        duplicated_identifiers = []

        for element in self:
            if element.identifier in identifiers:
                duplicated_identifiers.append(element.identifier)
                continue

            identifiers.add(element)

        if duplicated_identifiers:
            raise BotValidationSourceIdentifiersError(identifiers=duplicated_identifiers)
