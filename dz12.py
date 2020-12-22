import requests
import csv
from os import path
from random import randint


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
    fieldnames = ["Author", "Quote", "URL"]
    with open(path.join(csv_file), "w") as csv_file:
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


get_quotes(10)

