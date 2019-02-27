# -- encoding: utf-8 --
import configparser
import sys
import re
from pathlib import Path

# Global vars
LAC_FILE_EXTENSIONS = ['.lac', '.template', '.config']

def pathFromParent(parent_folder, current_folder):
    parent_parts = parent_folder.parts
    current_parts = current_folder.parts
    index = 0
    while(parent_parts[index] == current_parts[index]):
        parent_parts.pop(0)
        current_parts.pop(0)

    return Path('/'.join(current_parts))

if __name__ == "__main__":

    # Root folder input
    base_folder = input('Carpeta raiz: ')
    base_folder_path = Path(base_folder)
    if not base_folder_path.exists() or not base_folder_path.is_dir():
        print("La carpeta especificada no existe: {}".format(base_folder_path.resolve()))
        sys.exit(0)

    # Section RE input
    section_re_str = input('Expresión regular para sección: ')
    if not section_re_str:
        section_re_str = '.*'

    section_regex = re.compile(section_re_str)

    # Field RE input
    field_re_str = input('Expresión regular para campo: ')
    if not field_re_str:
        field_re_str = '.*'

    field_regex = re.compile(field_re_str, re.IGNORECASE)

    # List and process LAC files
    pending_folders = [base_folder_path]
    while pending_folders:
        current_folder_path = pending_folders.pop(0)

        for file_path in current_folder_path.iterdir():

            # If it is a folder add it to pending
            if file_path.is_dir():
                pending_folders.append(file_path)
                continue;

            # If it is a lac file analize it
            elif file_path.suffix in LAC_FILE_EXTENSIONS:
                print("{2}{0} {1} {0}".format('#'*12, file_path, '\n'*2))
                config = configparser.ConfigParser()
                config.read(file_path)
                sections = [sec for sec in config.sections() if section_regex.match(sec)]
                for section in sections:
                    print("{}{}[{}]".format('\n', ' '*2, section))

                    for field in config[section]:
                        if field_regex.match(field):
                            print("{}{} = {}".format(' '*4, field.upper(), config[section][field]))
