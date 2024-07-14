import sys


def get_cats_info(path):
    result = []

    try:
        header = ["id", "name", "age"]
        with open(path, 'r', encoding="utf-8") as fh:
            file_contents = fh.read()
            rows = file_contents.split('\n')
            for row in rows:
                numbers_list = {header[idx]: x for idx, x in enumerate(row.split(','))}
                if len(numbers_list) != 3:
                    raise Exception(f'File is corrupted.{path}\n')

                result.append(numbers_list)

    except FileNotFoundError as error:
        sys.stderr.write(f'File not found: {path}.\n {str(error)}\n')
    except IndexError as error:
        sys.stderr.write(f'File is corrupted: {path}.\n {str(error)}\n')
    except Exception as error:
        sys.stderr.write(str(error))

    return result


cats_info = get_cats_info("files/cats.txt")
print(cats_info)
