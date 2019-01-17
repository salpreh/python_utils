#!/usr/bin/python3
import sys
import io
from pathlib import Path
from PIL import Image

path_str = input("Ruta a carpeta de imágenes:")
path = Path(path_str)

if not path.exists() or not path.is_dir():
    print("La carpeta no existe: {}".format(path.resolve()))
    sys.exit(1)

images = [f for f in path.iterdir() if f.name.endswith(".jpg")]
corruptedImages = []
print("> Comprobando ficheros jpg ...\n")
for image in images:
    try:
        print(image.name)
        imageCheck = Image.open(image.resolve())
        imageCheck.load()

    except IOError:
        corruptedImages.append(image.name)

# Reporte errores
print("\n### REPROTE:{} imágenes dañadas ###\n".format(len(corruptedImages)))
for i, name in enumerate(corruptedImages, start=1):
    print("{:03d}: {}".format(i, name))
