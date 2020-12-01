import random

rand_list = [random.randint(1, 100) for _ in range(100)]
print(rand_list)

###################################

triangle = {key: tuple(random.randint(-10, 10) for _ in range(2)) for key in "ABCDF"}
print(triangle)
print(triangle["A"], type(triangle["A"]))


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

ages_list= [value_age.get("age") for  value_age in persons]
age_min = min(ages_list)
for index_dict in persons:
    if index_dict.get("age") == age_min:
        print(index_dict.get("name"))
print("**************************")
names_list = [value_name.get("name") for value_name in persons]
len_name_max = max([len(name) for name in names_list])
for name in names_list:
    if len(name) == len_name_max:
        print(name)
print("**************************")
mid_age = sum(ages_list) // len(ages_list)
print(mid_age, "лет")
#print(persons[0].values())
# print(persons[0].keys())
###################################
my_dict_1 = {'A': 8, 'B': 7, 'C': 5, 'D': 3, 'F': 56}
my_dict_2 = {'D': 23, 'L': 56, 'C': 23, 'Z': 7, 'Y': 1}

my_set = list(set(my_dict_1.keys()).intersection(my_dict_2.keys()))
print(my_dict_1.keys(), type(my_dict_1.keys()))
print(len(my_dict_1))
print(my_set)

my_set2 = list(set(my_dict_1.keys()).difference(my_dict_2.keys()))
print(my_set2)
print(list(my_dict_1.items())[1])
# my_new_dict = {my_dict_1.values() }
my_new_dict = {key: my_dict_1[key] for key in my_set2}
print(my_new_dict)
# my_dict = {key: None for key in my_dict_1.key().}
# print(my_dict)