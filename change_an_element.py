numbers = (1, 2, [3, 4], 5)

change_an_element = list(numbers)

change_an_element[2] = 99

numbers = tuple(change_an_element)\

print(numbers)
