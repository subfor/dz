value = int(input("Введите число: "))
#########
new_value = value / 2 if value < 100 else value * -1
print(new_value)
#########
new_value = 1 if value < 100 else 0
print(new_value)
#########
new_value = "True" if value < 100 else "False"
#print(type(new_value))
print(new_value)
#########
my_str = "Test string 123 QWE;+df-"

my_str_new = my_str.upper()
print(my_str_new)
#########
my_str_new = my_str.lower()
print(my_str_new)
#########
my_str_new = my_str * 2 if len(my_str) < 5 else my_str
print(my_str_new)
#########
my_str_new = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(my_str_new)
#########
res = ''
for symbol in my_str:
    if symbol.isalnum():
        res += symbol
print(res)
#########
res = ''
for symbol in my_str:
    if not symbol.isalnum():
        res += symbol
print(res)
#########
res = ''
for symbol in my_str:
    if not symbol.isalnum() and symbol !=" ":
        res += symbol
print(res)
