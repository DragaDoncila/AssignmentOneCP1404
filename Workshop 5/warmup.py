"""a: numbers[0] = 3
b: numbers[-1] = 2
c: numbers[3] = 1
d: numbers[:-1] = [3, 1, 4, 1, 5, 9]
e: numbers[3:4] = [1]
f: 5 in numbers = True
g: 7 in numbers = False
h: '3' in numbers = False
j: numbers + [6, 5, 3] = [3, 1, 4, 5, 9, 2, 6, 5, 3]"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# print(numbers[0])
# print(numbers[-1])
# print(numbers[3])
# print(numbers[:-1])
# print(numbers[3:4])
# print(5 in numbers)
# print(7 in numbers)
# print("3" in numbers)
# print(numbers + [6, 5, 3])

numbers[0] = 'ten'
print(numbers)
numbers[-1] = 1
print(numbers)
print(numbers[2:])
print(9 in numbers)