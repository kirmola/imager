from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
import pandas, json
from os import makedirs


csv_file = r"data/Quotes.csv"

file = pandas.read_csv(csv_file)


def main():
    makedirs("generated_images", exist_ok=True)

    quotes = []
    index = 1
    for each in zip(file["quote"], file["images"]):
        quotes.append(
            {
                "quote": each[0],
                "image": json.loads(each[1])["images"][0],
                "thumbnail": json.loads(each[1])["images"][1]
            }
    )

    for quote in quotes:
        length = len(quote["quote"])
        if length <= 230:
            current_x_position = 200
            current_y_position = 350
            font_size = 100
            width = 50

        elif 230 < length <= 330:
            current_x_position = 200
            current_y_position = 230
            font_size = 90
            width = 50

        elif 330 < length <= 430:
            current_x_position = 200
            current_y_position = 140
            font_size = 85
            width = 56


        elif 430 < length <= 530:
            current_x_position = 175
            current_y_position = 140
            font_size = 75
            width = 65


        elif 530 < length <= 630:
            current_x_position = 170
            current_y_position = 140
            font_size = 70
            width = 65

        else:
            pass

        image = Image.open("images/quote_bg.png")
        font = ImageFont.truetype("fonts/english/morningdew.ttf", size=font_size)
        text_to_write = wrap(quote["quote"], width=width)
        imageDrawing = ImageDraw.Draw(image)
        for each_piece in text_to_write:
            imageDrawing.text(font=font, text=each_piece, xy=(
                current_x_position, current_y_position), fill="white")
            current_y_position += 100
        image.save(f"generated_images/{quote["image"]}")

        thumbnail_size = (100,100)
        thumbnail = image.copy()
        thumbnail.thumbnail(thumbnail_size)
        thumbnail.save(f"generated_images/{quote["thumbnail"]}")
        image.close()
        thumbnail.close()
        print(f"Created: {index}")
        index += 1


if __name__ == "__main__":
    main()
