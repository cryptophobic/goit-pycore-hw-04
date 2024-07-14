import sys

from colorama import Fore
import argparse
from pathlib import *


def pick_style(path):
    # I have no idea why
    # return Fore.BLUE if path.is_dir() else Fore.GREEN
    # is not working
    if path.is_dir():
        return Fore.BLUE
    else:
        return Fore.GREEN


def recursive_walk(root: str, indent=0):
    root_path = Path(root)
    
    if not root_path.exists():
        raise FileNotFoundError(f"{root_path} does not exist")
    
    print(
        pick_style(root_path)
        + (" " * indent)
        + str(root_path.name))

    if not root_path.is_dir():
        return

    for path in sorted(root_path.iterdir(), key=lambda x: (not x.is_dir(), x.name)):
        if path.is_dir():
            recursive_walk(str(path), indent + 2)
        else:
            print(
                pick_style(path)
                + (" " * (indent + 2))
                + str(path.name))


def main(directory: str):
    try:
        recursive_walk(directory)
    except FileNotFoundError as error:
        sys.stderr.write(f"{Fore.RESET}Path not found: {str(error)}\n")
    except PermissionError as error:
        sys.stderr.write(f"{Fore.RESET}Cannot read the contents: {str(error)}\n")


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
