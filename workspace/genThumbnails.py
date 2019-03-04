# -*- encoding: utf-8 -*-
import sys
from PIL import Image
from pathlib import Path


# Global vars
THUMB_SIZE = 420
VALID_EXTENSIONS = ['.jpg', '.jpeg', '.JPG', '.JPEG']


def genThumbs(input_folder, thumb_folder, valid_ext=VALID_EXTENSIONS):
    # Get images in folder and process it
    images = [f for f in input_folder.iterdir() if f.suffix in valid_ext]
    if images:
        print('>> Procesing images...')
    else:
        print('>> Images not found. Valid extensions: {}'.format(valid_ext))
    for image in images:
        try:
            im = Image.open(image.resolve())
            if image.suffix == '.png':
                im = im.convert('RGB')

            # Check proportions and calculate final size
            orWidth, orHeight = im.size
            if orWidth >= orHeight:
                thWidth = THUMB_SIZE
                thHeight = round(orHeight / orWidth * THUMB_SIZE)

            else:
                thHeight = THUMB_SIZE
                thWidth = round(orWidth / orHeight * THUMB_SIZE)

            # Resize and save
            thumb_img = im.resize((thWidth, thHeight), Image.ANTIALIAS)
            thumb_path = thumb_folder / '{}.{}'.format(image.stem, 'jpg')
            thumb_img.save(thumb_path.resolve())
            print("> Image '{}' thumb generated".format(image.name))

        except IOError:
            print("> Error generating thumb for image '{}'".format(image.name))


if __name__ == '__main__':

    # User inputs
    in_folder = input('Path to images folder: ')
    in_folder_path = Path(in_folder)
    if not in_folder_path.exists() or not in_folder_path.is_dir():
        print("The folder not found: {}".format(in_folder_path.resolve()))
        sys.exit(0)

    out_folder = input('Folder to save thumbs (optional): ')
    if not out_folder:
        out_folder = str(in_folder_path.resolve()) / 'thumbs'

    out_folder_path = Path(out_folder)
    if not out_folder_path.exists():
        out_folder_path.mkdir(parents=True)

    genThumbs(in_folder_path, out_folder_path)

    print('>> Execution finished')
