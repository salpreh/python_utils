import sys
from pathlib import Path
from PIL import Image


ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png']

if __name__ == '__main__':

    # User Input
    src_path_str = input("Path to images folder: ")
    src_path = Path(src_path_str)

    if not src_path.exists() or not src_path.is_dir():
        print("Folder don't exist ({})".format(src_path.resolve()))
        sys.exit(0)

    dest_path_str = input("New image folder (optional): ")
    dest_path = src_path
    if dest_path_str:
        dest_path = Path(dest_path_str)

    if not dest_path.exists() or not dest_path.is_dir():
        print("Creating folder '{}'".format(dest_path.resolve()))
        dest_path.mkdir(parents=True)

    images = [f for f in src_path.iterdir() if f.suffix in ALLOWED_EXTENSIONS]

    if not images:
        print('> No images in the specified folder. Extensions enabled: {}'.format(ALLOWED_EXTENSIONS))
    else:
        print('> Procesing images ...')

    # Open and save images in 'jpg' format
    for image in images:
        try:
            image_obj = Image.open(image.resolve())
            new_img_path = dest_path / '{}.jpg'.format(image.stem)
            image_obj.save(new_img_path, 'jpeg', icc_profile=image_obj.info.get('icc_profile'))
            print(">> Image {} procesed".format(image.name))

        except IOError:
            print(">> Error while procesing image '{}'".format(image.name))

    print('> Execution finished!')
