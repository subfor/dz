my_str1 = "aabccccdfrx xx z"
my_str2 = "aa ccd f z"
my_list_new = []

my_unic = set(my_str1).intersection(set(my_str2))
my_list_new = [value for value in my_unic if my_str1.count(value) == 1 and my_str2.count(value) == 1]
print(my_str1)
print(my_str2)
print(my_list_new)