from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import docx


class DOCXIngestor(IngestorInterface):
    """Simple DOCX Ingestor."""

    extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses DOCX and returns list of quotes.
        Arguments:
            a {int} -- file path (str)
        Raises:
            Exception: if filetype cannot be ingested."""

        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception.')

        quotes = []

        doc = docx.Document(path)
        for line in doc.paragraphs:
            if line.text != "":
                try:
                    line.text.split(' - ')
                except Exception("Quote too long, or ' - ' missing"):
                    return False
                else:
                    parse = line.text.split(' - ')
                quote_text = parse[0].encode('utf-8')
                quote = QuoteModel(quote_text.decode('utf-8'), parse[1])
                quotes.append(quote)

        return quotes
