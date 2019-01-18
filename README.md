# atlUtils

A collection of python scripts and utilities.

* ***checkImages.py***: Check and list corrupted _.jpg_ images.

* ***resizeImages.py***: Resizes images keeping the proportions. The script asks for
the size of one side in pixels _(keep in mind that 100px at 254ppp is equal at 1cm, so for resize one side of the image to 15cm the input is 1500)_.

* ***excelLib.py***: Library to generate an spreadsheet from python lists _(Read methods pydoc to more details)_.

* ***renameFiles.py***: Renames files in a folder. Matches a keyword that must contain the file/s and replaces it for another word.

* ***openFolder***: Opens a folder in the explorer using a nickname _(only for Windows os)_.  Requires a config file with the nickname and the path to the folder. More details on the _Readme.md_ inside the config folder.
