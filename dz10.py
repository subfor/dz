import json
from os import path


def read_json(json_file: str):
    with open(path.join(json_file), "r") as file:
        result = json.load(file)
    return result


def sort_by_text_len(person: dict):
    text = person["text"].split(" ")
    return len(text)


def sort_by_name(person: dict):
    name = person["name"].split(" ")[-1]
    return name


def sort_by_death_date(person: dict):
    data = person["text"].split(" ")
    return None


persons = sorted(read_json("data.json"), key=sort_by_text_len)
print(persons)
persons = sorted(read_json("data.json"), key=sort_by_name)
print(persons)
