# a = b = c = 3
# a = 4
# a = b
# print(a)
# print(b)
# print(c)

my_string = '0123456789'
my_tuple = tuple(my_string)
print(my_tuple)
print(my_tuple[1], type(my_tuple[1]))
my_list = []
for index_tuple in my_tuple:
    # print(index_tuple, type(index_tuple))
    # print(index_tuple + index_tuple)
    for index_tuple_1 in my_tuple:
        print(index_tuple + index_tuple_1)

