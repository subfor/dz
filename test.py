
my_string = '0123456789'
my_tuple = tuple(my_string)
my_list = []

for index_tuple in my_tuple:
    for index_tuple_1 in my_tuple:
        num = int(index_tuple + index_tuple_1)
        my_list.append(num)
print(my_list)
