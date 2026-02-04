import os
import sys

from CSVFile import CSVFile
from JSONFile import JSONFile
from PickleFile import PickleFile


def get_file_handler(path):
    extension = os.path.splitext(path)[1].lower()

    if extension == ".csv":
        return CSVFile(path)
    elif extension == ".json":
        return JSONFile(path)
    elif extension == ".pkl":
        return PickleFile(path)
    else:
        raise ValueError(F"Unsupported file type: {extension}")


def main():
    if len(sys.argv) < 3:
        print("Usage: python reader.py <src> <dst> <change1> <change2> ...")
        sys.exit(1)


    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    if not os.path.isfile(src):
        print(f"Error: '{src}' is not a valid file.")
        directory = os.path.dirname(src) or "."
        print("Files in the same directory:")
        for name in os.listdir(directory):
            print(name)
        sys.exit(1)

    try:
        src_file = get_file_handler(src)
        dst_file = get_file_handler(dst)
    except ValueError as e:
        print(e)
        sys.exit(1)

    src_file.load(src)
    src_file.apply_changes(changes)
    src_file.display()
    lst_to_save = src_file.get_data()

    lst = [[1,2, 3, 4], [5, 6, 7]]
    dst_file.save(dst, lst_to_save)

if __name__ == "__main__":
        main()