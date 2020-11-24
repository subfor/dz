my_int = 23004000300
my_int_str = str(my_int)
count = my_int_str.count("0")
print(count)

#######################

my_int = 23004000300
print(len(str(my_int)) - len(str(int(str(my_int)[::-1]))))
# my_int_str = int("".join(my_int_str))
# my_int_str = len(str(my_int_str))