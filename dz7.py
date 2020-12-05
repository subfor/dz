"""изменил импорт"""
from random import randint

rand_list = [randint(1, 100) for _ in range(20)]
print(rand_list)

###################################
triangle = {key: tuple(randint(-10, 10) for _ in range(2)) for key in "ABC"}
print(triangle)


###################################
def my_print(my_str_: str):
    # print("***", my_str_, "***")
    my_list = ["***", my_str_, "***"]
    print("".join(my_list))


my_str = "I'm the string"
my_print(my_str)


###################################
persons = [{"name": "John", "age": 35}, {"name": "Bob", "age": 19}, {"name": "Jack", "age": 15},
           {"name": "Thomas", "age": 45}, {"name": "Richard", "age": 25}, {"name": "Richird", "age": 15}]


ages_list = [value_age.get("age") for value_age in persons]
age_min = min(ages_list)
for index_dict in persons:
    if index_dict.get("age") == age_min:
        print(index_dict.get("name"))


print("**************************")
names_list = [value_name.get("name") for value_name in persons]
len_name_max = max([len(name) for name in names_list])
max_name = [print(name) for name in names_list if len(name) == len_name_max]

print("**************************")
mid_age = sum(ages_list) // len(ages_list)
print(mid_age, "лет")


###################################
my_dict_1 = {'A': 8, 'B': 7, 'C': 5, 'D': 3, 'F': 56}
my_dict_2 = {'D': 23, 'L': 56, 'C': 23, 'Z': 7, 'Y': 1, 'B': 1}

repeat_keys_dicts = list(set(my_dict_1.keys()).intersection(my_dict_2.keys()))
print(repeat_keys_dicts)


##############################
unique_keys_dict1 = list(set(my_dict_1.keys()).difference(my_dict_2.keys()))
print(unique_keys_dict1)


###############################
my_new_dict = {key: my_dict_1[key] for key in unique_keys_dict1}
print(my_new_dict)

###############################
union_dict = {}
unique_keys_in_dicts = list(set(my_dict_1.keys()).difference(my_dict_2.keys())) \
                       + list(set(my_dict_2.keys()).difference(my_dict_1.keys()))
for key in unique_keys_in_dicts:
    if key in my_dict_1:
        union_dict[key] = my_dict_1.get(key)
    else:
        union_dict[key] = my_dict_2.get(key)
for key in repeat_keys_dicts:
    union_dict[key] = list((my_dict_1.get(key), my_dict_2.get(key)))
print(union_dict)
