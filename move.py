from PIL import Image
import os

downloadsFolder = "/Users/Matias/Downloads/"
picturesFolder = "/Users/Matias/Pictures/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            image = Image.open(downloadsFolder + filename)
            image.save(picturesFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        # Se puede aplicar con otros tipos de archivos, por ejemplo para .mp3
        # if extension in [".mp3"]:
        #     musicFolder = "/Users/Matias/Music/"
        #     os.rename(downloadsFolder + filename, musicFolder + filename)