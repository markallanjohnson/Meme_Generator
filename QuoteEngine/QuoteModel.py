class QuoteModel:
    """encapsulate body and author of quote."""

    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def __repr__(self):
        """representation of QuoteModel."""

        return f'{self.body} - {self.author}'
