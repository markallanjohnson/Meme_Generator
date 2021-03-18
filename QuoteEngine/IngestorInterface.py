from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Simple Ingestor Interface."""

    extension = []

    @classmethod
    def can_ingest(cls, path):
        """Check if file type can be ingested."""

        ext = path.split('.')[-1]
        return ext in cls.extension

    @classmethod
    @abstractmethod
    def parse(self, path: str) -> List[QuoteModel]:
        pass


def add_quotes(parse):
    """Adds quotation marks around a quote if none are present."""

    if parse[0] != '"':
        if parse[-1] != '"':
            quote = f'"{parse}"'
        else:
            quote = f'"{parse}'
    elif parse[-1] != '"':
        quote = f'{parse}"'
    else:
        quote = parse
    return quote
