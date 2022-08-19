from email.mime import image
from PIL import Image # python3 -m pip install Pillow

import os

downloadsFolder = "/Users/Matias/Downloads/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            image = Image.open(downloadsFolder + filename)
            image.save(downloadsFolder + "compressed_"+filename, optimize=True, quality=60)