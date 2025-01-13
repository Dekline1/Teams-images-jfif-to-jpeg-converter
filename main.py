import os
from PIL import Image

os.chdir(os.path.dirname(os.path.abspath(__file__)))

input_folder = "Input"
output_folder = "Output"

if not os.path.exists(input_folder):
    os.makedirs(input_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for image in os.listdir(input_folder):
    if image.endswith('.jfif'):
        image_path = os.path.join(input_folder, image)
        with Image.open(image_path) as img:
            jpegName = os.path.join(output_folder, os.path.splitext(image)[0] + '.jpeg')
            img.convert('RGB').save(jpegName, "JPEG")
