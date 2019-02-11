import sys
import re
from pathlib import Path
from PIL import Image, ImageFile

# Global vars
INCH_IN_MM = 25.4
VALID_EXTENSIONS = ['.jpg', '.JPG', '.jpeg', '.JPEG']

def MMtoPx(sizeMM, ppi=254):
    return round(sizeMM * ppi / INCH_IN_MM)

if __name__ == "__main__":

    if (len(sys.argv) > 2 and sys.argv[1] == '-r'):
        try:
           ppi  = int(sys.argv[2])
        except ValueError:
            print("Error casting resolution input number: {}".format(sys.argv[2]))

    else:
        ppi = 254

    path_str = input("Path to images folder: ")
    path = Path(path_str)

    width_str = input("Final_width (MM): ")
    wanted_width = int(width_str)

    orientation = input("Horizontal/Veritcal (h/v): ")
    vertical = False
    orientation = orientation[0]
    if orientation not in "hv":
        print("Valid values: h (Horizontal), v (Vertical)")

    elif orientation == 'v':
        vertical = True

    if not path.exists() or not path.is_dir():
        print("Folder not found: {}".format(path.resolve()))
        sys.exit(1)

    images = [f for f in path.iterdir() if f.suffix in VALID_EXTENSIONS]
    corruptedImages = []
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    print("> Checking jpg files ...\n")
    for image in images:
        try:
            imageEditor = Image.open(image.resolve())
            imageEditor.load()
            orWidth, orHeight = imageEditor.size

            # Image resize
            if vertical and orWidth > orHeight or not vertical and orWidth < orHeight:
                final_height = MMtoPx(wanted_width, ppi)
                final_width = MMtoPx(orWidth * wanted_width / orHeight, ppi)

            else:
                final_width = MMtoPx(wanted_width, ppi)
                final_height = MMtoPx(orHeight * wanted_width / orWidth, ppi)
                print("{}x{} -> Calc data: orH {}, finalw {}, orWidth {}".format(final_width, final_height, orHeight, final_width, orWidth))

            newImage = imageEditor.resize((final_width, final_height), Image.ANTIALIAS)
            newImage.save(image.resolve(), "JPEG", quality=100)
            print("{} resized".format(image.name))

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
        print("\n### REPROTE:{} corrupted jpg images ###\n".format(len(corruptedImages)))
        for i, name in enumerate(corruptedImages, start=1):
	           print("{:03d}: {}".format(i, name))
