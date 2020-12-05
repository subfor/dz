import os


def read_file(domains_file: str):
    with open(os.path.join(path_dir, domains_file), 'r') as file:
        lines = file.readlines()
    result = [value_line.strip()[1:] for value_line in lines]
    return result


def read_names(names_file: str):
    with open(os.path.join(path_dir, names_file), 'r') as file:
        lines = file.readlines()
    line = [list((value_line.strip().replace('\t', " ")).split(" ")) for value_line in lines]
    names_list = [index[1] for index in line]
    return names_list


path_dir = "domains"
print(read_file("domains.txt"))
print(read_names("names.txt"))

