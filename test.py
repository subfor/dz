from random import randint, choice, uniform
from string import ascii_lowercase, digits

# random_dict = {}
# for _ in range(randint(5, 20)):
#     random_bool = choice([True, False])
#     random_key = "".join(choice(ascii_lowercase) for _ in range(5))
#     random_value_digit = choice([randint(-100, 100), uniform(0, 1)])
#     random_value = choice([random_bool, random_value_digit])
#     random_dict[random_key] = random_value
# # my_dict = {"".join(choice(ascii_lowercase) for _ in range(5)): choice([choice([True, False]), choice([randint(-100, 100), uniform(0, 1)])]) for _ in range(randint(5, 20))}
# print(random_dict)
# for  value in random_dict:
#     print(value, random_dict[value])

n = range(randint(3, 10))
my_list = [[choice("01") for _ in n] for _ in range(randint(3, 10))]
print(my_list)