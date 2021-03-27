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
            """

        try:
            Image.open(img_path)
        except Exception("Not a valid image path."):
            return

        if width > 500:
            width = 500
            print("Width set to maximum size, 500px")
        elif width <= 0:
            width = 500
            print("Width must be a positive value. Width set to 500px")

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

        #feels like this could be improved...
        print(f'text_w: {text_w}')
        print(f'width: {width}')
        if text_w < width:
            x_pos = randint(0, width - text_w)
            y_pos = randint(0, min(500, h) - text_h)
            draw.text((x_pos, y_pos), quote, (255,255,255))
        else:
            quote_list = quote.split()
            x_cursor = 0
            lines = int(text_w / width) + 1
            height = int(lines * text_h)
            temp_x = 0
            y_cursor = randint(0, min(500, h) - height)
            temp_width = width
            for word in quote_list:
                word_width = draw.textsize(word)[0]
                temp_word_width = word_width
                space_width = draw.textsize(" ")[0]
                if x_cursor + word_width >= width:
                    y_cursor += text_h
                    temp_x = temp_width - temp_word_width
                draw.text((x_cursor - temp_x, y_cursor), word,
                          (255,255,255))
                x_cursor += word_width + space_width - temp_x
                temp_x = 0

        output_file_name = os.path.join(self.output_dir,
                               'memes',
                               "outputmeme_{}.jpg".format(randint(0,10000)))
        image.save(output_file_name)
        image.close()
        return output_file_name
