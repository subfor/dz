import re

my_str = "Server response 2003 from 123.0.0.12, Wrong 123-0-0-12"

pattern = r"[0-9]+"  # все числа из строки
# pattern = r"\d+"
pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"  # символ . это один любой символ

my_str = "Kolobok 235-234 BC"
pattern = r"\d+"

result = re.findall(pattern, my_str)
print(result)