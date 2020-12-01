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

