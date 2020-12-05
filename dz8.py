import sys
import os

path_dir = "domains"


def read_file(file_read: str):
    with open(os.path.join(path_dir, file_read), 'r') as file:
        lines = file.readlines()
    result = [value_line.strip()[1:] for value_line in lines]
    return result


print(read_file("domains.txt"))
