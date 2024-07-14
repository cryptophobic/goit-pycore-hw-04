import statistics
import sys


def total_salary(path):
    try:
        with open(path, 'r', encoding="utf-8") as fh:
            file_contents = fh.read()
            rows = file_contents.split('\n')
            numbers_list = [int(x.split(',')[1]) for x in rows]
            return sum(numbers_list), statistics.mean(numbers_list)
    except FileNotFoundError as error:
        sys.stderr.write(f'File not found. {path}.\n {str(error)}\n')
    except ValueError as error:
        sys.stderr.write(f'Value error. {path}.\n {str(error)}\n')
    except IndexError as error:
        sys.stderr.write(f'File is corrupted. {str(error)}\n'
                         "Please use comma separated format, every row should contain only 2 "
                         "columns, 2nd one must be decimal integer.\n")

    return None, None


total, average = total_salary("files/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
