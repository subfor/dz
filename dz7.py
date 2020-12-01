import random

rand_list = [random.randint(1, 100) for _ in range(100)]
print(rand_list)

###################################

triangle = {key: tuple(random.randint(-10, 10) for _ in range(2)) for key in "ABC"}
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
midl_age = sum(ages_list) // len(ages_list)
print(midl_age, "лет")
###################################
