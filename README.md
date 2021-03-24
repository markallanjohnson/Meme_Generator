# Meme Generator

Multimedia application to dynamically generate memes.

## Overview

Python code that implements a command-line tool, as well as Flask, to generate
and save memes. Memes created from random quotes contained within
./_data/DogQuotes as well as a random image from ./_data/photos/dog. Quotes and
Image may also be specified by user in command line. Custom meme may be created
by user in web browser.

Optional Command Line Interface arguments:
-h, --help
--path
--body
--author

where "-- path" is path of the image.


## Interface

### meme.py

Driven by 'meme.py' script. Run 'python meme.py ... ... ...' at the command
line to invoke the program that will call the code.

A random meme will be generated and saved by running 'python meme.py'

User may input path of image, body, and author, to create their own meme.

for CLI to work, pdftotext.exe must be downloaded.
pdftotext may be downloaded from https://www.xpdfreader.com/download.html.

ex:

```
#random meme
$ python3 meme.py
./static/memes\outputmeme_8815.jpg

#Using random image, apply this quote: "I'm a dog" - Travis Barker
#Note that if you specify a quote, you must also specify an author and
#vice versa.
$ python3 meme.py --body '"I am a dog"'  --author "Travis Barker"
./static/memes\outputmeme_5730.jpg

#You can also specify an image using its path
$ python3 meme.py --path "./_data/photos/dog/xander_1.jpg"
./static/memes\outputmeme_6213.jpg
```

### app.py

invoking 'app.py' script runs the flask server. user may generate random memes
or create a meme by supplying arguments in the web form.

ex:

```
$ python3 app.py
* Serving Flask app "app" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
User must then navigate to http://127.0.0.1:5000/ in a web browser to access
content.

## Modules

### MemeEngine

MemeEngine module (class initialized using desired output directory for meme)
contains just one method, "make_meme", which takes image path, quote text, and
author, creates a meme using this information, and returns the memes directory.
-requires PIL and randint from random to run.

### QuoteEngine

QuoteModel defines a QuoteModel class, which contains body and author of quote.

Ingestor Interface is an abstract base class used by CSVIngestor, DOCXIngestor,
PDFIngestor, and TXTIngestor. Contains can_ingest classmethod to determine if
file type is ingestible by Ingestor, along with an abstract method, parse, used
to parse file content.
- requires typing from List to run, as well as ABC and abstractmethod from abc.

CSVIngestor defines the abstract method, parse, to parse CSV files only.
returns a list of QuoteModel objects.
- requires typing from List and pandas to run.

DOCXIngestor defines the abstract method, parse, to parse DOCX files only.
returns a list of QuoteModel objects.
- requires typing from List and docx to run.

PDFIngestor defines the abstract method, parse, to parse PDF files only.
returns a list of QuoteModel objects.
- requires typing from List and subprocess, randint from random, and remove from
os.

TXTIngestor defines the abstract method, parse, to parse TXT files only.
returns a list of QuoteModel objects.
- requires typing from List to run as well as random.

Ingestor defines the abstract method, parse, and utilizes the four ingestors
listed above to parse a CSV, DOCX, PDF, or TXT file, and return a list of
QuoteModel objects
- requires typing from List to run.

All ingestor classes take just one argument: the filepath of the document
that contains quotes.
