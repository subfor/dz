import json
import csv
from random import randint, choice, uniform
from string import ascii_lowercase, digits
from os import path


def generate_str():
    mystr = []
    result_string = ""
    random_len = randint(100, 1000)

    while len(result_string) <= random_len:
        random_sentense = []
        for _ in range(randint(3, 12)):
            # random_sentense = ["".join(choice(ascii_lowercase) for _ in range(randint(2, 12))) for _ in range(randint(3, 10))]
            random_word = ("".join(choice(ascii_lowercase) for _ in range(randint(2, 12))))
            random_digit = ("".join(choice(digits) for _ in range(randint(1, 5))))
            if randint(1, 10) // 2:
                random_sentense.append(random_word)
            else:
                random_sentense.append(random_digit)
        mystr.append(random_sentense)
        # print(*[' '.join(m) for m in mystr], sep=' ')
        flat_list = [item for sublist in mystr for item in sublist]
        result_string = f'{" ".join(flat_list)}\n'
    for value in mystr:
        if not value[0].isdigit():
            value[0] = value[0].capitalize()
        if len(value) >= 3:
            for _ in range(randint(1, len(value)) // 3):
                s = randint(0, len(value) - 1)
                value[s] = f"{value[s][:-1]}{choice(',:')}"
        value[-1] = f"{value[-1][:-1]}{choice('.!?')}"
    flat_list = [item for sublist in mystr for item in sublist]
    result_string = f'{" ".join(flat_list)}\n'
    if len(result_string) > 998:
        result_string = f"{result_string[:998 - len(result_string)]}{choice('.!?')}\n"
    return result_string


def generate_dict():
    random_dict = {}
    for _ in range(randint(5, 20)):
        random_bool = choice([True, False])
        random_key = "".join(choice(ascii_lowercase) for _ in range(5))
        random_value_int = randint(-100, 100)
        random_value_float = uniform(0, 1)
        random_dict[random_key] = choice([random_bool, random_value_int, random_value_float])
    return random_dict


def generete_list():
    n = range(randint(3, 10))
    my_list = [[choice("01") for _ in n] for _ in range(randint(3, 10))]
    return my_list


def write_file(file_to_write: str):
    ext = file_to_write[file_to_write.rfind("."):]
    if ext == ".csv":
        with open(path.join(file_to_write), "w") as csv_file:
            data = generete_list()
            writer = csv.writer(csv_file)
            writer.writerows(data)
    elif ext == ".json":
        with open(path.join(file_to_write), "w") as json_file:
            json.dump(generate_dict(), json_file)
    elif ext == ".txt":
        with open(path.join(file_to_write), "w") as txt_file:
            txt_file.write(generate_str())
    else:
        print("Unsupported file format")


# write_file("ewre1.jsonqq")
# write_file("ewre1.csv")
# write_file("ewre1.json")
# write_file("ewre1.txt")
a = generate_str()
print(a, len(a))