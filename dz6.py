my_list = ["qwed", "23efadf", "dsf4fr", "adesce", "jdffa", "dfgr"]
my_list_new =[]

# for index, value in enumerate(my_list):
#     if (index + 1) % 2:
#         my_list_new.append(value[::-1])
#     else:
#         my_list_new.append(value)
my_list_new = [value[::-1] if (index + 1) % 2 else value for index, value in enumerate(my_list) ]
print(my_list)
print(my_list_new)
##########################
my_list = ["aqwed", "23efadf", "dsf4fr", "adesce", "jdffa", "dfgr"]
my_list_new = []

# for value in my_list:
#     if value[0] == "a":
#         my_list_new.append(value)
my_list_new = [value for value in my_list if value[0] == "a"]
print(my_list_new)
##########################

my_list = ["aqwed", "23efadf", "dsf4fr", "adesce", "jdffa", "dfgr"]
my_list_new = []

my_list_new = [value for value in my_list if value.find("a") > -1]
print(my_list_new)
##########################
my_list = ["23", "aqwed", "23efadf", "76", "dsf4fr", "adesce", "jdffa", "7","dfgr"]
my_list_new = []

my_list_new = [value for value in my_list if value.isdigit()]
print(my_list_new)
##########################
my_str = "aabccccdrx xx r"
my_list_new = []

my_set_tmp = list(set(my_str))
my_set = my_set_tmp.copy()
my_set.sort()
my_list_new = [value for value in my_set if my_str.count(value) == 1]
print(my_str)
print(my_list_new)
#########################
my_str1 = "aabccccdrx xx r"
my_str2 = "aa ccd f"
my_list_new = []

my_list_new = list(set(my_str1).intersection(set(my_str2)))
print(my_list_new, type(my_list_new))
###########################
