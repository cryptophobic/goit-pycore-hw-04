import sys
from colorama import Fore
import argparse
from pathlib import *


def recursive_walk(root: str, indent=0):
    for path in Path(root).iterdir():
        print((Fore.BLUE if path.is_dir() else Fore.GREEN) + (' ' * indent) + str(path.name))
        if path.is_dir():
            recursive_walk(str(path), indent + 2)


def main(directory: str):
    try:
        recursive_walk(directory)
    except FileNotFoundError as error:
        sys.stderr.write(f'{Fore.RESET}Path not found: {str(error)}\n')
    except PermissionError as error:
        sys.stderr.write(f'{Fore.RESET}Cannot read the contents: {str(error)}\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directory",
        help="Path to the directory",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    main(**vars(args))
