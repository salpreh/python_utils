import sys
import re
from pathlib import Path
from PIL import Image, ImageFile

if __name__ == "__main__":

    path_str = input("Ruta a carpeta de imágenes: ")
    path = Path(path_str)

    width_str = input("Anchura final: ")
    wanted_width = int(width_str)

    orientation = input("Horizontal/Veritcal (h/v): ")
    vertical = False
    orientation = orientation[0]
    if orientation not in "hv":
        print("Valores validos orientación: h (Horizontal), v (Vertical)")

    elif orientation == 'v':
        vertical = True

    if not path.exists() or not path.is_dir():
        print("La carpeta no existe: {}".format(path.resolve()))
        sys.exit(1)

    images = [f for f in path.iterdir() if f.name.endswith(".jpg")]
    corruptedImages = []
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    print("> Comprobando ficheros jpg ...\n")
    for image in images:
        try:
            imageEditor = Image.open(image.resolve())
            imageEditor.load()
            orWidth, orHeight = imageEditor.size

            # Image resize
            if vertical and orWidth > orHeight or not vertical and orWidth < orHeight:
                final_height = wanted_width
                final_width = round(orWidth * final_height / orHeight)

            else:
                final_width = wanted_width
                final_height = round(orHeight * final_width / orWidth)

            newImage = imageEditor.resize((final_width, final_height), Image.ANTIALIAS)
            newImage.save(image.resolve(), "JPEG", quality=100)
            print("{} redimensionada".format(image.name))

        except IOError:
            corruptedImages.append(image.name)

        except Image.DecompressionBombError as ex:
            pixel_size_re = re.compile("Image size .(\d+).*")
            print(str(ex))
            match = pixel_size_re.match(str(ex))
            if match:
                print("\n[DecompressionBombAlert] La imagen excedió el limite de pixels")
                increase_answer = input("Incrementar limite de pixels en imagen (s/n): ")
                if len(increase_answer) > 0 and increase_answer[0] in 's':
                    Image.MAX_IMAGE_PIXELS = int(match.group(1))
                    images.append(image)

                else:
                    corruptedImages.append(image.name)

    # List corrupted images
    if len(corruptedImages) > 0:
        print("\n### REPROTE:{} imágenes dañadas ###\n".format(len(corruptedImages)))
        for i, name in enumerate(corruptedImages, start=1):
	           print("{:03d}: {}".format(i, name))
