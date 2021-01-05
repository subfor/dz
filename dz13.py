from os import path
from random import randint, choice
from string import ascii_lowercase


class EmailGenerator:

    def __init__(self, domains_file: str, names_file: str):
        self._path_dir = "domains"
        self._domains_file = domains_file
        self._names_file = names_file
        self.domains = self._read_domains()
        self.names = self._read_names()

    def __str__(self):
        return f"len domains = {len(self.domains)}, len names = {len(self.names)}"

    def _read_domains(self):
        domain_list = []
        try:
            with open(path.join(self._path_dir, self._domains_file), 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("File not found")
            return domain_list
        domain_list = [value_line.strip()[1:] for value_line in lines]
        return domain_list

    def _read_names(self):
        names_list = []
        try:
            with open(path.join(self._path_dir, self._names_file), 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("File not found")
            return names_list
        line = [list((value_line.strip().replace('\t', " ")).split(" ")) for value_line in lines]
        names_list = [index[1] for index in line]
        return names_list

    def generate_email(self, count_emails=1):
        my_email_list = []
        try:
            for _ in range(count_emails):
                random_name = str(choice(self.names)).lower()
                random_domain = choice(self.domains)
                random_domain_name = "".join(choice(ascii_lowercase) for _ in range(randint(5, 7)))
                my_email = f"{random_name}.{randint(100, 999)}@{random_domain_name}.{random_domain}"
                my_email_list.append(my_email)
                res = ", ".join(my_email_list)
        except (UnboundLocalError, IndexError):
            res = ""
        return res


email = EmailGenerator("domains.txt", "names.txt")
print(email.domains)
print(email.names)
print(email)
email = email.generate_email()
print(email)
