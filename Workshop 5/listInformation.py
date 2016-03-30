"""Prompts the user for five numbers and displays interesting information about
said numbers."""

numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number in your list is {}".format(numbers[0]))
print("The last number in your list is {}".format(numbers[-1]))
print("The smallest number in your list is {}".format(min(numbers)))
print("The largest number in your list is {}".format(max(numbers)))
print("The average of your numbers is {}".format(sum(numbers)/len(numbers)))
print("Your list in sorted order is {}".format(sorted(numbers)))
print("Your list in reverse order is {}".format(sorted(numbers, reverse=True)))