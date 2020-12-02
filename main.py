from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import time


start_time = time.time()


INPUT_DIR = 'input'
OUTPUT_DIR = 'output'
WATERMARK_FILE = 'watermark.png'


def add_watermark_with_image(input_image, watermark_image, position):
    # open source image file and get this image size
    input_image = Image.open(input_image)
    input_image_width, input_image_height = input_image.size

    # calculate watermark size relative to the source image size
    watermark_image_width = input_image_width/100 * 10
    watermark_image_height = input_image_height / 100 * 10

    # open watermark image and resize it
    watermark_image = Image.open(watermark_image)
    watermark_image = watermark_image.resize((round(watermark_image_width), round(watermark_image_height)))

    # create new image form source image and watermark
    transparent = Image.new('RGBA', (input_image_width, input_image_height), (0, 0, 0, 0))
    transparent.paste(input_image, (0, 0))
    transparent.paste(watermark_image, position, mask=watermark_image)
    transparent.save(f'{OUTPUT_DIR}/{os.path.splitext(os.path.basename(file))[0]}_watermarked.png')


def add_watermark_with_text(input_image, watermark_text, position):
    # open source image file and get this image size
    input_image = Image.open(input_image)
    input_image_width, input_image_height = input_image.size
    drawing = ImageDraw.Draw(input_image)

    # set text styles
    font_color = (3, 8, 12)
    font_size = round(input_image_width/100 * 4)
    font = ImageFont.truetype("fonts/APEXMK3_MEDIUM.ttf", font_size)

    # draw text and save image
    drawing.text(position, watermark_text, fill=font_color, font=font)
    input_image.save(f'{OUTPUT_DIR}/{os.path.splitext(os.path.basename(file))[0]}_watermarked.png')


if __name__ == '__main__':
    input_files = os.listdir(INPUT_DIR)
    #input_files = input_files[:1]
    for file in input_files:
        # add_watermark_with_image(f'{INPUT_DIR}/{file}', WATERMARK_FILE, position=(0, 0))
        add_watermark_with_text(f'{INPUT_DIR}/{file}', 'Тестовый текст', position=(0, 0))
    print("time elapsed: {:.2f}s".format(time.time() - start_time))
