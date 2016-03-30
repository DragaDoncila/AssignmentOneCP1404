"""Get a number of quickpicks from user and generate that many quickpicks"""

from random import randint

num_quickpicks = int(input("How many quick picks? "))
quickpick_list = []
for i in range(num_quickpicks):
    while len(quickpick_list) != 6:
        randnum = randint(1, 45)
        if randnum in quickpick_list:
            randnum = randint(1, 45)
        else:
            quickpick_list.append(randnum)

    # print it outside for loop, as that means a full list
    # clear before next iteration
    for number in sorted(quickpick_list):
        print("{:3d}".format(number), end="")
    print()
    quickpick_list = []

