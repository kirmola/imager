from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
import pandas as pd
import json
from os import makedirs
import concurrent.futures

csv_file = r"data/Quotes.csv"
file = pd.read_csv(csv_file)

def generate_image(quote):
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
        return

    images = ["3"]
    for bg_image in images:
        image = Image.open(f"images/{bg_image}.png")
        font = ImageFont.truetype("fonts/english/morningdew.ttf", size=font_size)
        text_to_write = wrap(quote["quote"], width=width)
        imageDrawing = ImageDraw.Draw(image)
        for each_piece in text_to_write:
            imageDrawing.text(
                font=font, text=each_piece, xy=(current_x_position, current_y_position), fill="white"
            )
            current_y_position += 100

        image_name = f"{quote['quote_id']}-{bg_image}.png"
        thumbnail_name = f"{quote['quote_id']}-{bg_image}-thumb.png"
        image.save(f"generated_images/{image_name}")
        thumbnail_size = (100, 100)
        thumbnail = image.copy()
        thumbnail.thumbnail(thumbnail_size)
        thumbnail.save(f"generated_images/{thumbnail_name}")
        image.close()
        thumbnail.close()

def main():
    makedirs("generated_images", exist_ok=True)
    quotes = []
    for each in zip(file["quote"], file["quote_id"]):
        quotes.append(
            {
                "quote": each[0],
                "quote_id": each[1],
            }
        )

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(generate_image, quotes)

if __name__ == "__main__":
    main()