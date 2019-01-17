import shutil
import os
import re
from pathlib import Path

inputFolderPath = Path("C:\\Users\\Salva\\Desktop\\Plantillas Navidad\\Rename-pls\\CALSOBREM\\EU03")
INC_COUNTER = 1
MULTIFILE = True


def genNewName(newName):
    """
    Genera el nuevo nombre de la plantilla expandiendo las etiquetas especiales
    que pueda contener
    """
    increment_tag = '(INC)'
    if increment_tag in newName:
        global INC_COUNTER
        sub_start = newName.find(increment_tag)
        genName = "{}{:02d}{}".format(newName[:sub_start], INC_COUNTER,
                                      newName[sub_start + len(increment_tag):])

        INC_COUNTER += 1
        return genName

    else:
        return newName


def resetCounter():
    """
    Resetea contador global
    """
    global INC_COUNTER
    INC_COUNTER = 1


if __name__ == "__main__":

    while True:
        inputFolder = input("Ruta a carpeta de ficheros: ")
        if inputFolder == "":
            break;

        inputFolderPath = Path(inputFolder)
        if not inputFolderPath.exists() or not inputFolderPath.is_dir():
            print("No existe una carpeta en la ruta: {}".format(inputFolderPath.resolve()))


        name = input("Nombre actual de fichero: ")
        newName = input("Nuevo nombre: ")
        nameRE = re.compile("{}(.*)".format(name))
        os.chdir(inputFolderPath.resolve())

        # Recorremos ficheros de carpeta
        lastName = "%[]*"
        lastNewName = ""
        for file in inputFolderPath.iterdir():
            if nameRE.match(file.name):
                match = nameRE.match(file.name)

                # Controlar ficheros con mismo nombre pero diferente extensión
                if MULTIFILE and file.stem == lastName:
                    os.rename(file.name, lastNewName + match.group(1))

                else:
                    lastName = file.stem
                    lastNewName = genNewName(newName)
                    os.rename(file.name, lastNewName + match.group(1))


                print("File {} renamed".format(file.name))

        resetCounter()
