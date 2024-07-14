import sys
from colorama import Fore
import argparse
from pathlib import *


def pick_style(path: Path):
    # I have no idea why
    # return Fore.BLUE if path.is_dir() else Fore.GREEN
    # is not working
    if path.is_dir():
        return Fore.BLUE
    else:
        return Fore.GREEN


# dirs[n] is True means the current file on level n is the last file in directory
def format_indentation(dirs: tuple) -> str:

    indent = len(dirs)

    if indent == 1:
        return " ┗ " if dirs[0] is True else " ┣ "
    elif indent > 1:
        return "".join([format_indentation((x, ))
                        if idx == indent - 1
                        else ("   " if x is True else " ┃ ") for idx, x in enumerate(dirs)])

    return ""


def recursive_walk(root: str, dirs=(True, )):
    root_path = Path(root)
    if not root_path.exists():
        raise FileNotFoundError(f"{root_path} does not exist")

    print(Fore.RESET
          + format_indentation(dirs)
          + ("📦" if root_path.is_dir() else "📜")
          + pick_style(root_path)
          + str(root_path.name)
          + ("/" if root_path.is_dir() else ""))

    if not root_path.is_dir():
        return

    sorted_list = sorted(root_path.iterdir(), key=lambda x: (not x.is_dir(), x.name))
    number = len(sorted_list)

    for idx, path in enumerate(sorted_list):
        is_the_last_file = idx == number - 1
        if path.is_dir():
            recursive_walk(str(path), dirs + (is_the_last_file, ))
        else:
            print(
                Fore.RESET
                + format_indentation(dirs + (is_the_last_file, ))
                + "📜"
                + pick_style(path)
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
