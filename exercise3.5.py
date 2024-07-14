import glob
import sys
from colorama import Fore
import argparse
from pathlib import *


def format_indentation(indent: int, dirs) -> str:
    if indent == 0:
        return ""
    elif indent == 1:
        return "┗ " if dirs[0] is True else "┣ "
    else:
        length = len(dirs)
        res = ""
        for idx, x in enumerate(dirs):
            if idx == length - 1:
                res = res + format_indentation(1, (x, ))
            else:
                res = res + "  " if x is True else '┃ '

        return res


def recursive_walk(root: str, indent=0, dirs=()):
    number = len(glob.glob(root + '/*'))

    for idx, path in enumerate(Path(root).iterdir()):
        is_the_last_file = idx == number - 1
        if path.is_dir():
            print(Fore.RESET + format_indentation(indent, dirs + (is_the_last_file, )) + '📦' + Fore.BLUE + str(path.name) + '/')
            recursive_walk(str(path), indent + 1, dirs + (is_the_last_file, ))
        else:
            print(Fore.RESET + format_indentation(indent, dirs + (is_the_last_file, )) + '📜' + Fore.GREEN + str(path.name))


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
