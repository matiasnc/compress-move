"""
Descripcion del script:
Comprime archivos de un tipo especificado y pregunta si se desea conservar los archivos originales.
"""

__author__ = "Matias Nahuel Calderon"
__version__ = "1.0"
__email__ = "mn.calderon97@gmail.com"
__status__ = ""

from PIL import Image
import os

downloadsFolder = "/Users/Matias/Downloads/"
picturesFolder = "/Users/Matias/Pictures/"

if __name__ == "__main__":
    #while True:
        delete = input('¿Eliminar archivos originales? [Y/N]')
        for filename in os.listdir(downloadsFolder):
            name, extension = os.path.splitext(downloadsFolder + filename)

            if extension in [".jpg", ".jpeg", ".png"]:
                image = Image.open(downloadsFolder + filename)
                image.save(picturesFolder + "compressed_" + filename, optimize=True, quality=60)
                if any(delete == f for f in ['YES', 'yes', 'Y', 'y']):
                    os.remove(downloadsFolder + filename)
                    print(name + ": " + extension  + '. Se elimina archivo original.')
                elif any(delete == f for f in ['NO', 'no', 'N', 'n']):
                    print(name + ": " + extension + '. Se conserva archivo original.')
                else:
                    print('El comando ingresado no es valido.') #Iterar a pregunta
                    break
            else:
                print('No se encuentra archivos con el formato buscado.')
                break

        # Se puede aplicar con otros tipos de archivos, por ejemplo para .mp3
        # if extension in [".mp3"]:
        #     musicFolder = "/Users/Matias/Music/"
        #     os.rename(downloadsFolder + filename, musicFolder + filename)