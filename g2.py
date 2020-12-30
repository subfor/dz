# def sum_numbers(text: str) -> int:
#     res = 0
#     my_list = text.split(" ")
#     for value in my_list:
#         if value.isdigit():
#             res += int(value)
#     return res
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(sum_numbers('5 plus 6 is'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert sum_numbers('hi') == 0
#     assert sum_numbers('who is 1st here') == 0
#     assert sum_numbers('my numbers is 2') == 2
#     assert sum_numbers('This picture is an oil on canvas '
#  'painting by Danish artist Anna '
#  'Petersen between 1845 and 1910 year') == 3755
#     assert sum_numbers('5 plus 6 is') == 11
#     assert sum_numbers('') == 0
#     print("Coding complete? Click 'Check' to earn cool rewards!")


# def checkio(array: list) -> int:
#     res = 0
#     if array:
#         for index, value in enumerate(array):
#             if not index % 2:
#                 res += value
#         res = res * array[-1]
#     return res
#
#
# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     print('Example:')
#     print(checkio([0, 1, 2, 3, 4, 5]))
#
#     assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
#     assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
#     assert checkio([6]) == 36, "(6)*6=36"
#     assert checkio([]) == 0, "An empty array = 0"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
# def left_join(phrases: tuple) -> str:
#     # my_str = ",".join(phrases)
#     # x = my_str.replace("right", "left")
#     return ",".join(phrases).replace("right", "left")
#
#
# if __name__ == '__main__':
#     print('Example:')
#     print(left_join(("left", "right", "left", "stop")))
#
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
#     assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
#     assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
#     assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
# import re
#
#
# def checkio(words: str) -> bool:
#     result = re.search(r'\s+'.join([r'[^\d\s]+']*3), words)
#     res = True if result else False
#     return res
# #return True if re.search(r'([A-Z|a-z]+\s[A-Z|a-z]+\s[A-Z|a-z]+)', words) else False
# #return bool( findall(r"(\D+\s\D+\s\D+)",words))
# # These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     print('Example:')
#     print(checkio("Hello World hello"))
#
#     assert checkio("Hello World hello") == True, "Hello"
#     assert checkio("He is 123 man") == False, "123 man"
#     assert checkio("1 2 3 4") == False, "Digits"
#     assert checkio("bla bla bla bla") == True, "Bla Bla"
#     assert checkio("Hi") == False, "Hi"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
import re


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    res = re.findall(r"(^\s\W+\s)", text)
    print(res)
    return "".join(res)


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")

