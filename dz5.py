my_int = 23004000300
my_int_str = str(my_int)
count = my_int_str.count("0")
print(count)

#######################

my_int = 230040003000
len_zero = len(str(my_int)) - len(str(int(str(my_int)[::-1])))
print(len_zero)

######################

my_list_1 = [1,2,3,4,5 ]
my_list_2 = [10, 15, 20, 25]
my_result = []
# for index, value in enumerate(my_list_1):
    # print(index, value)
    # if index % 2:
    #     my_result.append(value)
    # print(my_list_1[index])
for value_1 in my_list_1:
    if not value_1 % 2:
        my_result.append(value_1)
for value_2 in my_list_2:
    if value_2 % 2:
        my_result.append(value_2)
print(my_result)
##################
my_list = [1,2,3,4,5]
new_list = []
for index, value in enumerate(my_list):
    if index > 0:
        new_list.append(value)
new_list.append(my_list[0])
print(new_list)
###################
my_list = [1,2,3,4,5]
last = my_list.pop()
my_list.insert(0, last)
print(my_list)
####################
my_str = "43 больше чем 34 но меньше чем 56"
my_list = my_str.split(" ")
tmp = 0

for value in my_list:
    if value.isdigit():
        res = tmp + int(value)
        tmp = res
print(res)

##################
my_str = 'abcdereryze'
index_start = 0
index_stop = 1
my_list = []
len_str = len(my_str)
for value in range(int(len_str // 2)):
    my_list.append(my_str[index_start] + my_str[index_stop])
    index_start += 2
    index_stop += 2
if len_str % 2:
    my_list.append(my_str[index_start] + '_')
print(my_list)
##################
my_str = "My_long str"
l_limit = "o"
r_limit = "t"
a = my_str.find(l_limit)
sub_str = my_str[my_str.find(l_limit) + 1:my_str.find(r_limit)]
print(sub_str)
##################
my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print(sub_str)