numbers = [1, 3, 5, 6, 7, -2]

new_numbers = []
# for number in numbers:
#     if number > 0:
#         new_numbers.append(number ** 2)

new_numbers = [number ** 2 for number in numbers]

print(new_numbers)