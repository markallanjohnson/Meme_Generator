from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """Main ingestor class. Encapsulates all ingestors."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Returns list of quotes for any supported filetype.

        Supported filetypes: CSV, DOCX, PDF, TXT."""

        csv = CSVIngestor()
        docx = DOCXIngestor()
        pdf = PDFIngestor()
        txt = TXTIngestor()
        ingestors = [csv, docx, pdf, txt]

        for ingestor in ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise Exception("Filetype Not Supported.")
