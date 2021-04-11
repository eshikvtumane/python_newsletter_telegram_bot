from typing import List


class BotError(Exception):
    pass


class BotValidationSourceIdentifiersError(BotError):
    def __init__(self, identifiers: List[str]):
        message = ', '.join(identifiers)

        super().__init__(message)
