import os
import sys
import configparser
from pathlib import Path
from subprocess import call

ZIP_PASS = None
CONFIG_ROUTE = './config-files/zipIt.ini'


def loadPass(pass_id):
    config_path = Path(CONFIG_ROUTE)
    if not config_path.exists():
        print("Error: Config file not found ({})".format(config_path.resolve()))
        return False

    config = configparser.ConfigParser()
    config.read(config_path)
    if config.has_option('ZipConfig', pass_id):
        global ZIP_PASS
        ZIP_PASS = config['ZipConfig'][pass_id]
        return True

    else:
        print("'{}' identifier not found. Available identifiers: ".format(pass_id))
        for field in config['ZipConfig']:
            print('\t* {}'.format(field))

    return False

if __name__ == "__main__":

    # Check command line flags
    if len(sys.argv) > 2:
        if sys.argv[1] == '-p':
            ZIP_PASS = sys.argv[2]

        elif sys.argv[1] == '-i':
            if not loadPass(sys.argv[2]):
                print("Error loading password from config file. Finishing execution.")
                sys.exit(0)

    # User input
    folder = input("Folder to zip: ")
    folder_path = Path(folder)
    if not folder_path.exists():
        print("Folder does not exists: {}".format(folder_path.resolve()))
        sys.exit(0)

    folder_out = input("Output folder (optional): ")
    if not folder_out:
        folder_out = folder_path.parent.resolve()

    folder_out_path = Path(folder_out)
    if not folder_out_path.exists() or not folder_out_path.is_dir():
        print("Output folder does not exists: {}".format(folder_out_path.resolve()))

    # Generate zip file
    print("Processing {} for ZIP".format(folder_path.name))
    zip_file_path = folder_out_path / (folder_path.name + ".zip")
    print("Creating ZIP {}".format(zip_file_path.name))
    if zip_file_path.exists():
        zip_file_path.unlink()

    # Zip call aruments
    zip_call_args = ['7z', 'a', '-y', '-r']
    if ZIP_PASS:
        zip_call_args.append("-p{}".format(ZIP_PASS))

    zip_call_args.append(str(zip_file_path.resolve()))
    zip_call_args.append(os.path.join(str(folder_path.resolve()), "*.*"))

    call(zip_call_args)
