from random import randint, choice
from string import ascii_lowercase, digits


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
        for index, value in enumerate(mystr):
            if not value[0].isdigit():
                value[0] = value[0].capitalize()
            if len(value) >= 3 and index != 0:
                for _ in range(randint(1, len(value)) // 7):
                    s = randint(0, len(value) - 1)
                    value[s] = f"{value[s][:-1]}{choice(',:')}"
            value[-1] = f"{value[-1][:-1]}{choice('.!?')}"
        # print(*[' '.join(m) for m in mystr], sep=' ')
        flat_list = [item for sublist in mystr for item in sublist]
        # print(flat_list, len(flat_list))
        result_string = f'{" ".join(flat_list)}\n'
    # b = list(a)
    print(result_string)
    print(len(result_string))
    if len(a) > 998:
        result_string = f"{result_string[:998 - len(a)]}{choice('.!?')}\n"
    return a
for _ in range(3):
    x = generate_str()
    print(x, len(x))
