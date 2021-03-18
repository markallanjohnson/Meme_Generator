from .IngestorInterface import IngestorInterface, add_quotes
from typing import List
from .QuoteModel import QuoteModel
import random


class TXTIngestor(IngestorInterface):
    """Simple TXT Ingestor."""

    extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses TXT and list of quotes.
        Arguments:
            a {int} -- file path (str)
        Raises:
            Exception: if filetype cannot be ingested."""

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
            return False

        quotes = []

        f = open(path, 'r', encoding='utf-8-sig')
        for line in f:
            line = line.rstrip()
            if line != "":
                try:
                    line.split(' - ')
                except Exception("Quote too long, or ' - ' missing"):
                    return False
                else:
                    parse = line.split(' - ')
                quote = add_quotes(parse[0])
                quote_object = QuoteModel(quote, parse[1])
                quotes.append(quote_object)

        return quotes
