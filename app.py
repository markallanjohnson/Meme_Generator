import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, TXTIngestor
from random import randint


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    parser = Ingestor()
    quotes = []
    for file in quote_files:
        parsed = parser.parse(file)
        if parsed != []:
            quotes.append(parsed)

    images_path = "./_data/photos/dog/"

    imgs = []
    for f in os.listdir(images_path):
        img = os.path.join(images_path, f)
        if img is not None:
            imgs.append(img)

    return quotes, imgs


@app.route('/')
def meme_rand():
    """Generate a random meme."""

    quotes, imgs = setup()
    img = random.choice(imgs)
    quote = random.choice(random.choice(quotes))

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""

    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""

    if request.method == 'POST':
        result = request.form
        img = result['image_url']
        body = result['body']
        author = result['author']

        page = requests.get(img)
        temp_image = './tmp/images/temp_img.jpg'
        with open(temp_image, 'wb') as f:
            f.write(page.content)

        temp_txt = f'./tmp/quotes/temp_txt.txt'
        with open(temp_txt, 'w') as f:
            f.write(f'{body} - {author}')

        ingestor = Ingestor()
        quote = ingestor.parse(temp_txt)[0]
        body = quote.body
        author = quote.author

        path = meme.make_meme(temp_image, body, author)

        os.remove(temp_image)
        os.remove(temp_txt)

    return render_template('meme.html', path=path)

@app.errorhandler(500)
def internal_server_error(e):
    """Create 500 error handler."""
    os.remove('./tmp/images/temp_img.jpg')
    os.remove(f'./tmp/quotes/temp_txt.txt')
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run()
