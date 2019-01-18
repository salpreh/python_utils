import subprocess
import configparser
from pathlib import Path
import sys

# Global Vars
AVAILABLE_ROUTES = {}
CONFIG_ROUTE = './config-files/openFolder.ini'


def loadConfig():
    config_path = Path(CONFIG_ROUTE)
    if not config_path.exists():
        print("Error: Fichero de configuración no encontrado ({})".format(config_path.resolve()))
        return False

    config = configparser.ConfigParser()
    config.read(config_path)
    for field in config['AvailableRoutes']:
        AVAILABLE_ROUTES[field] = config['AvailableRoutes'][field]

    return True

if __name__ == "__main__":

    if not loadConfig():
        print('No se ha podido cargar configuración')
        sys.exit(0)

    if len(sys.argv) > 1:
        folder_id = sys.argv[1]

    else:
        print("\n")
        for key, path in AVAILABLE_ROUTES.items():
            print("{} -> {}".format(key, path))

        folder_id = input("\nCarpeta a abrir: ")

    folder_path_str = AVAILABLE_ROUTES.get(folder_id, None)
    if not folder_path_str:
        print("Identificador incorrecto")
        sys.exit(0)

    folder_path = Path(folder_path_str)
    if not folder_path.exists() or not folder_path.is_dir():
        print("[Error configuración] La ruta no existe ({})".format(folder_path.resolve()))

    subprocess.Popen(r'explorer "{}"'.format(folder_path.resolve()))
