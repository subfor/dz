import json
import re
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
    data = person["years"]
    pattern = r"\d+"
    year = int(re.findall(pattern, data)[1])
    data_of_death = year * -1 if "BC" in data else year
    return data_of_death


print(read_json("data.json"))
persons = sorted(read_json("data.json"), key=sort_by_name)
print(persons)
persons = sorted(read_json("data.json"), key=sort_by_death_date)
print(persons)
persons = sorted(read_json("data.json"), key=sort_by_text_len)
print(persons)