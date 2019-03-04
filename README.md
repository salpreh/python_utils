# python_utis

A collection of python scripts and utilities.

---
### Setup instructions
Clone the repository and initialize a python virtual enviroment in the repo folder:
```sh
pythom -m venv venv
```

Acivate the virtual enviroment and use the `requirements.txt` file to install the required libraries locally to the enviroment

**Windows:**
```sh
cd [repoFolder]
venv/Scripts/activate.bat
pip install -r requirements.txt
```
**Shell:**
```sh
cd [repoFolder]
source venv/bin/activate
pip install -r requirements.txt
```
(Additional info on python [virtual enviroments](https://docs.python.org/3/tutorial/venv.html) and [documentation](https://docs.python.org/3/library/venv.html))

---
### Scripts list
* ***checkImages.py***: Check and list corrupted _.jpg_ images.

* ***resizeImages.py***: Resizes images keeping the proportions. The script asks for
the size of one side in millimeters and resized at 254ppp of resolution by default. Use the flag **'-r'** to change the output resolution.

* ***excelLib.py***: Library to generate an spreadsheet from python lists _(Read methods pydoc to more details)_.

* ***renameFiles.py***: Renames files in a folder. Matches a keyword that must contain the file/s and replaces it for another word.

* ***openFolder***: Opens a folder in the explorer using a nickname _(only for Windows os)_.  Requires a config file with the nickname and the path to the folder. More details in the _Readme.md_ inside the config folder.

* ***listIniValues.py***: List recursively keys and values from`.ini` files. Uses regular expresions to select sections and keys.

* ***changeIniValue.py***: Similar to `listLacProperty.py` script. Use a regular expresión to select section and key and then input the new value for the matched fields.

* ***addIniValue.py***: Similar to `listLacProperty.py` script. Use a regular expresión to select section and key and then input the new value for the matched fields. The script don't overwrite by default if the key already exists use **'-f'** flag. To explore recursively the sub-directories use **'-r'** flag.

* ***compareFiles***: Compare if two files are exactly the same.

* ***zipIt***: Generates a zip file from a folder. You can use the flag **'-p'** to use a password for the zip. Additionaly you can load a password from a config file using an id with **'-i'** flag. The config file is an `.ini` file with pairs id/pass. More info in _Readme.md_ file inside config folder. (The script requires 7z installed)
