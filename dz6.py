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
#######################$###