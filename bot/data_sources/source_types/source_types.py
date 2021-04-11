class BaseSource:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
        self.identifier = None

        self._generate_identifier()

    def _generate_identifier(self):
        source_name_transform = self.name.replace(' ', '_')
        self.identifier = f'{self.get_class_name()}_{source_name_transform}'

    def __repr__(self):
        return f'<{self.get_class_name()}>: {self.name}>'

    def get_class_name(self):
        return self.__class__.__name__


class RssSource(BaseSource):
    pass
