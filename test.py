my_list = [1, 55, 22, 107, 234, 0, 100, 23, 923, 2, 8, 105]
for value in my_list:
    if value > 100:
        print(value)
############
my_list = [1, 55, 22, 107, 234, 0, 100, 23, 923, 2, 8, 105]
my_results = []
for value in my_list:
    if value > 100:
        my_results.append(value)
print(my_results)
#############
my_list = [1, 55, 22, 107, 234, 0, 100, 23, 923, 2, 8, 105]
if len(my_list) < 2:
    my_list.append(0)
elif len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)
#############
try:
    value = float(input("Введите число с запятой: "))
    print(value ** -1)
except (ValueError, ZeroDivisionError):
    print("Это не число с запятой!")


##############
# my_string = '0123456789'
# my_tuple = tuple(my_string)
# my_list = []
#
# for index_tuple in my_tuple:
#     for index_tuple_1 in my_tuple:
#         num = int(index_tuple + index_tuple_1)
#         my_list.append(num)
# print(my_list)
