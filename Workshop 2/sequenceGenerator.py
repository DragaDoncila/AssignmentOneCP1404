from math import sqrt

MENU = """(E)vens
(O)dds
(S)quares
(P)erfect?
(C)hange Range
(Q)uit"""

lower_bound = int(input("Please enter a number: "))
upper_bound = int(input("Please enter a number higher than the first: "))

while lower_bound > upper_bound:
    print("I thought my instructions asked for a larger number entered second?")
    lower_bound = int(input("Please enter a number: "))
    upper_bound = int(input("Please enter a number higher than the first: "))

print(MENU)
choice = input(">>>").lower()
while choice != "q":

    if choice == "e":
        if lower_bound % 2 == 0:
            for i in range(lower_bound, upper_bound, 2):
                print(i, end=" ")
        else:
            for i in range(lower_bound + 1, upper_bound, 2):
                print(i, end=" ")
        print("\nThese were the even numbers in range")

    elif choice == "o":
        if lower_bound % 2 == 0:
            for i in range(lower_bound + 1, upper_bound, 2):
                print(i, end=" ")
        else:
            for i in range(lower_bound, upper_bound, 2):
                print(i, end=" ")
        print("\nThese were the odd numbers in range")

    elif choice == "s":
        for i in range(lower_bound, upper_bound):
            print("{}^2={}".format(i, i**2), end=" ")
        print("\nThese were the squares of numbers in range")

    elif choice == "p":
        for i in range(lower_bound, upper_bound):
            if sqrt(i) % 1 == 0:
                print("{} is a perfect square".format(i))
            else:
                print("{} is not a perfect square".format(i))

    elif choice == "c":
        lower_bound = int(input("Please enter a number: "))
        upper_bound = int(input("Please enter a number higher than the first: "))
        while lower_bound > upper_bound:
            print("I thought my instructions asked for a larger number entered second?")
            lower_bound = int(input("Please enter a number: "))
            upper_bound = int(input("Please enter a number higher than the first: "))

    else:
        print("This is not a valid choice")

    print(MENU)
    choice = input(">>>").lower()

print("Finished.")
