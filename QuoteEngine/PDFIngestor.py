from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
from random import randint
import subprocess
from .TXTIngestor import TXTIngestor
from os import remove


class PDFIngestor(IngestorInterface):
    """Simple PDF Ingestor"""

    extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses PDF and returns list of quotes.
        Requires pdftotext to be installed on the system.

        Arguments:
            a {path} -- file path (str)
        Raises:
            Exception: if filetype cannot be ingested."""

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception.')

        temp_file = f'{randint(0,1000000)}.txt'
        cmd = ['pdftotext','-layout', path, temp_file]
        with open(temp_file, 'w+') as f:
            p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
            parse_txt = TXTIngestor.parse(temp_file)
        f.close()
        remove(temp_file)
        return parse_txt
