from .IngestorInterface import IngestorInterface, add_quotes
from typing import List
from .QuoteModel import QuoteModel
import pandas


class CSVIngestor(IngestorInterface):
    """Simple CSV Ingestor."""

    extension = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses CSV and returns list of quotes.
        Arguments:
            a {int} -- file path (str)
        Raises:
            Exception: if filetype cannot be ingested."""

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception.')

        quotes = []

        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            quote = add_quotes(row['body'])
            quote_model = QuoteModel(quote, row['author'])
            quotes.append(quote_model)

        return quotes
