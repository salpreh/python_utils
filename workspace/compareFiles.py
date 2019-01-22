import hashlib
import sys
from hmac import compare_digest
from pathlib import Path


def generateHash(file_path, hash_alg='blake2b', chunk_size=4096):
    """
    Generate the hexdigest of a given file.
    args:
        file_path (pahtlib.Path): Path to a file.
        hash_alg (str): [Optional] Hash algorithm. By default 'blake2b'.
        chunk_size (int): [Optioal] Chunk size in bytes. By default 4kB.

    return (str):
        Hash code generated from the file
    """
    hash = hashlib.new(hash_alg)
    with open(file_path, 'rb') as file:
        chunk = file.read(chunk_size)
        while chunk:
            hash.update(chunk)
            chunk = file.read(chunk_size)

    return hash.hexdigest()


if __name__ == "__main__":

    # Ask for user input
    file_path_str = input("First file path: ")
    file_path1 = Path(file_path_str)
    if not file_path1.exists() or file_path1.is_dir():
        print("File not found ({})".format(file_path1.resolve()))
        sys.exit(0)

    file_path_str = input("Second file path: ")
    file_path2 = Path(file_path_str)
    if not file_path2.exists() or file_path2.is_dir():
        print("File not found ({})".format(file_path2.resolve()))
        sys.exit(0)

    # Check files hashes
    hash_str1 = generateHash(file_path1)
    hash_str2 = generateHash(file_path2)
    if compare_digest(hash_str1, hash_str2):
        print('\nSame file!')
    else:
        print('\nDifferent files')
