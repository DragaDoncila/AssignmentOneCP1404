finished = False
result = 0

while not finished:
    try:
        number = int(input("Please enter a number: "))
        result = number
        finished = True
    except ValueError:
        print("Please enter a VALID integer: ")
print("Valid result is:", result)

