from PIL import Image, ImageFont, ImageDraw
import os
from random import randint

class MemeEngine:
    """Meme Engine class.

    Arguments:
        a {output_dir} -- output file path (str)
    """

    def __init__(self, output_dir:str):
        self.output_dir = output_dir


    def make_meme(self, img_path:str, text:str, author:str, width=500) -> str:
        """Creates meme and returns meme folder path.

        Arguments:
            a {img_path} -- path of input Image (str)
            b {text} -- quote text (str)
            c {author} -- author of quote (str)
            d {width} -- defaults to 500. maxwidth is also 500 (int)
        Raises:
            Exception: If file path is not valid.
            Exception: If width greater than 500.
            """

        try:
            Image.open(img_path)
        except Exception("Not a valid image path."):
            return

        if width > 500:
            width = 500
            print("Width Set to max size, 500px.")
            
        image = Image.open(img_path)
        w, h = image.size
        image.thumbnail([width, h], Image.ANTIALIAS)

        draw = ImageDraw.Draw(image)
        quote = f'{text} - {author}'
        quote = quote.replace(u'\u2019', "'").encode('latin-1')

        try:
            text_w, text_h = draw.textsize(quote)
        except Exception:
            quote = quote.encode('latin-1', 'replace')

        text_w, text_h = draw.textsize(quote)
        width_pos = randint(0, width - text_w)
        height_pos = randint(0, min(500, h) - text_h)
        draw.text((width_pos, height_pos), quote, (255,255,255))
        output_file_name = os.path.join(self.output_dir,
                               'memes',
                               "outputmeme_{}.jpg".format(randint(0,10000)))
        image.save(output_file_name)
        image.close()
        return output_file_name
