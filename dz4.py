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
#############
my_list = [1, 55, 22, 107, 234, 0, 100, 23, 923, 2, 8, 105]
my_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for  index in my_indexes:
    print(my_list[index])
#############
my_list_1 = [1, 55, 22, 107, 234, 0, 100, 23, 923, 2, 8, 105]
my_list_2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
my_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for index in my_indexes:
    print("(", my_list_1[index], ",", my_list_2[index], ")")
##############
my_string = '0123456789'
my_tuple = tuple(my_string)
my_list = []

for value_1 in my_tuple:
    for value_2 in my_tuple:
        num = int(value_1 + value_2)
        my_list.append(num)
print(my_list)
