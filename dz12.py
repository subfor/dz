import requests
import csv
from os import path
from random import randint
import re
import json


def get_quote():
    url = "http://api.forismatic.com/api/1.0/"
    params = {"method": "getQuote",
              "format": "json",
              "key": randint(1, 999999),
              "lang": "ru"}
    r = requests.get(url, params=params, timeout=None)
    quote = r.json()
    return quote


def sort_by_name(person: list):
    name = person[0]
    return name


def write_to_csv(list_quotes, csv_file="quote.csv"):
    with open(path.join(csv_file), "w") as csv_file:
        fieldnames = ["Author", "Quote", "URL"]
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(fieldnames)
        for row in list_quotes:
            writer.writerow(row)
    return None


def get_quotes(count_q=1):
    count = 0
    list_quotes = []
    list_quotes_csv = []
    while count < count_q:
        quote = get_quote()
        if quote not in list_quotes and quote["quoteAuthor"]:
            list_quotes.append(quote)
            list_quotes_csv.append([quote["quoteAuthor"], quote["quoteText"], quote["quoteLink"]])
            count += 1
            print(quote["quoteAuthor"], ":", quote["quoteText"])
    list_quotes_csv = sorted(list_quotes_csv, key=sort_by_name)
    write_to_csv(list_quotes_csv)
    return list_quotes_csv


def read_authors(authors_file="authors.txt"):
    with open(path.join(authors_file), 'r') as file:
        lines = file.readlines()
    authors_list_tmp = [line.strip() for line in lines if
                        "birthday" in (line.lower()).strip() or "death" in (line.lower()).strip()]
    authors_list = [autor_line for autor_line in authors_list_tmp if "author" in autor_line.lower()
                    or "creator" in autor_line.lower() or "the master" in autor_line.lower()
                    or "poet" in autor_line.lower()]
    return authors_list


def create_dict_authors(list_authors: list):
    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    result_dict_list = []
    for line in list_authors:
        index_start_name = line.find("- ") + 2
        index_end_name = line.find("'s")
        name = line[index_start_name:index_end_name]
        pattern = r"[0-9]{1,2}"
        result = re.findall(pattern, line)
        day = result[0]
        year = f"{result[1]}{result[2]}"
        month = months[line.split()[1]]
        result_dict_list.append({"name": name, "date": f'{day}/{month}/{year}'})
    return result_dict_list


def write_json(authors_dicts_list, json_authors="authors.json"):
    with open(path.join(json_authors), "w") as json_file:
        json.dump(authors_dicts_list, json_file, indent=1)
    return None


# get_quotes(10)
write_to_csv(get_quotes(10))
list_authors = read_authors()
print(list_authors)
authors_dict = create_dict_authors(list_authors)
print(authors_dict)
write_json(authors_dict)
