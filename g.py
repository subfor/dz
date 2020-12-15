# my_tpl = (6, 2, 9, 4, 3, 9)
#
# my = (my_tpl[0], my_tpl[2], my_tpl[-2])
# my1 = (value[key] for value in my_tpl for key in (0, 2, -2))
# print(my1)

# def first_word(text: str) -> str:
#     """
#         returns the first word in a given text.
#     """
#
#     return text.split(" ")[0]
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(first_word("Hello world"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert first_word("Hello world") == "Hello"
#     assert first_word("a word") == "a"
#     assert first_word("hi") == "hi"
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def is_acceptable_password(password: str) -> bool:
#     # result = True if len(password) > 6 else False
#     return True if len(password) > 6 else False
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_acceptable_password('short12'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def number_length(a: int) -> int:
#     # your code here
#     return len(str(a))
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(number_length(10))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert number_length(10) == 2
#     assert number_length(0) == 1
#     assert number_length(4) == 1
#     assert number_length(44) == 2
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def end_zeros(num: int) -> int:
#     # zeros = len(str(num)) - len(str(int(str(num)[::-1]))) if not num == 0 else 1
#     return len(str(num)) - len(str(int(str(num)[::-1]))) if not num == 0 else 1
# # return len(str(num)) - len(str(num).strip('0'))
#
# if __name__ == '__main__':
#     print("Example:")
#     print(end_zeros(0))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert end_zeros(0) == 1
#     assert end_zeros(1) == 0
#     assert end_zeros(10) == 1
#     assert end_zeros(101) == 0
#     assert end_zeros(245) == 0
#     assert end_zeros(100100) == 2
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# from typing import Iterable
#
#
# def remove_all_before(items: list, border: int) -> Iterable:
#
#     return items[items.index(border):] if border in items else items
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
#     assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
#     assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
#     assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
#     assert list(remove_all_before([], 0)) == []
#     assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
#     print("Coding complete? Click 'Check' to earn cool rewards!")
from string import ascii_uppercase


# def is_all_upper(text: str) -> bool:
#     result = True
#     for value in text:
#         if value.islower():
#             result = False
#     return result
#
#
# # my_list_new = [value for value in my_set if my_str.count(value) == 1]
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_all_upper('ALL UPPER'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_all_upper('ALL UPPER') == True
#     assert is_all_upper('all lower') == False
#     assert is_all_upper('mixed UPPER and lower') == False
#     assert is_all_upper('') == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# from typing import Iterable
#
#
# def replace_first(items: list) -> Iterable:
#     # if items == [] or len(items) == 1:
#     #     return items
#     # else:
#     #     result_items = items[1:]
#     #     result_items.append(items[0])
#     if len(items) > 1:
#         result_items = items[1:]
#         result_items.append(items[0])
#         return result_items
#     return items
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(list(replace_first([1, 2, 3, 4])))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
#     assert list(replace_first([1])) == [1]
#     assert list(replace_first([])) == []
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def max_digit(number: int) -> int:
#     digit_list = [int(value) for value in list(str(number))]
#     digit_max = max(digit_list) if number > 0 else 0
#     return digit_max
# # return int(max(str(number)))
#
# if __name__ == '__main__':
#     print("Example:")
#     print(max_digit(0))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert max_digit(0) == 0
#     assert max_digit(52) == 5
#     assert max_digit(634) == 6
#     assert max_digit(1) == 1
#     assert max_digit(10000) == 1
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def split_pairs(a):
#     index_0 = 0
#     index_1 = 1
#     my_list = []
#     len_str = len(a)
#     for value in range(int(len_str // 2)):
#         my_list.append(a[index_0] + a[index_1])
#         index_0 += 2
#         index_1 += 2
#     if len_str % 2:
#         my_list.append(a[index_0] + '_')
#
#     return my_list
# import re
#
# # def split_pairs(a):
# #     a = a + "_"
# #     return re.findall(r"\w{2}", a)
#
# if __name__ == '__main__':
#     print("Example:")
#     print(list(split_pairs('abcd')))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(split_pairs('abcd')) == ['ab', 'cd']
#     assert list(split_pairs('abc')) == ['ab', 'c_']
#     assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
#     assert list(split_pairs('a')) == ['a_']
#     assert list(split_pairs('')) == []
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# def beginning_zeros(number: str) -> int:
#     count = 0
#     for value in number:
#         if value != "0":
#             return count
#         else:
#             count += 1
#     return count
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(beginning_zeros('100'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert beginning_zeros('100') == 0
#     assert beginning_zeros('001') == 2
#     assert beginning_zeros('100100') == 0
#     assert beginning_zeros('001001') == 2
#     assert beginning_zeros('012345679') == 1
#     assert beginning_zeros('0000') == 4
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def nearest_value(values: set, one: int) -> int:
#     values = list(sorted(values))
#     if one < values[0]:
#         return values[0]
#     elif one > values[-1]:
#         return values[-1]
#     for index, value in enumerate(values):
#         if values[index] < one < values[index + 1]:
#             if abs(values[index] - one) <= abs(values[index + 1] - one):
#                 res = values[index]
#             else:
#                 res = values[index + 1]
#         elif value == one:
#             res = one
#
#     return res
#
# if __name__ == '__main__':
#     print("Example:")
#     print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
#     assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
#     assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
#     assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
#     assert nearest_value({-1, 2, 3}, 0) == -1
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# def between_markers(text: str, begin: str, end: str) -> str:
#     """
#         returns substring between two given markers
#     """
#     # your code here
#     return text[text.find(begin) + 1: text.rfind(end)]
#
#
# if __name__ == '__main__':
#     print('Example:')
#     print(between_markers('What is >apple<', '>', '<'))
#
#     # These "asserts" are used for self-checking and not for testing
#     assert between_markers('What is >apple<', '>', '<') == "apple"
#     assert between_markers('What is [apple]', '[', ']') == "apple"
#     assert between_markers('What is ><', '>', '<') == ""
#     assert between_markers('>apple<', '>', '<') == "apple"
#     print('Wow, you are doing pretty good. Time to check it!')
#
# def correct_sentence(text: str) -> str:
#     """
#         returns a corrected sentence which starts with a capital letter
#         and ends with a dot.
#     """
#     # text = text.capitalize() + "." if text[-1] != "." else text.capitalize()
#     return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(correct_sentence("greetings, friends"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert correct_sentence("greetings, friends") == "Greetings, friends."
#     assert correct_sentence("Greetings, friends") == "Greetings, friends."
#     assert correct_sentence("Greetings, friends.") == "Greetings, friends."
#     assert correct_sentence("hi") == "Hi."
#     assert correct_sentence("welcome to New York") == "Welcome to New York."
#
#     print("Coding complete? Click 'Check' to earn cool rewards!")
# def is_even(num: int) -> bool:
#     # rez = True if not num % 2  else False
#     return not num % 2
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(is_even(2))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert is_even(2) == True
#     assert is_even(5) == False
#     assert is_even(0) == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")

