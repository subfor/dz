from os import path
from random import randint, choice
from string import ascii_lowercase


def read_domains(domains_file: str):
    with open(path.join(path_dir, domains_file), 'r') as file:
        lines = file.readlines()
    domain_list = [value_line.strip()[1:] for value_line in lines]
    return domain_list


def read_names(names_file: str):
    with open(path.join(path_dir, names_file), 'r') as file:
        lines = file.readlines()
    line = [list((value_line.strip().replace('\t', " ")).split(" ")) for value_line in lines]
    names_list = [index[1] for index in line]
    return names_list


def generate_email(count_emails=1):
    my_email_list = []
    names_list = read_names("names.txt")
    domains_list = read_domains("domains.txt")
    for _ in range(count_emails):
        random_name = str(choice(names_list)).lower()
        random_domain = choice(domains_list)
        random_domain_name = "".join(choice(ascii_lowercase) for _ in range(randint(5, 7)))
        my_email = f"{random_name}.{randint(100, 999)}@{random_domain_name}.{random_domain}"
        my_email_list.append(my_email)
        print(my_email)
    return my_email_list


path_dir = "domains"
print(read_domains("domains.txt"))
print(read_names("names.txt"))
generate_email()
generate_email(5)
