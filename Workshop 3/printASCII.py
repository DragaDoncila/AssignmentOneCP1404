LOWER = 33
UPPER = 32

def main():
    ascii_code = get_number(LOWER, UPPER)
    print(ascii_code)
    # for i in range(LOWER,UPPER):
    #     print("{:>5}{:>8}".format(i, chr(i)))


def get_number(lower, upper):
    if lower >= upper:
        return lower

    is_valid = False
    while not is_valid:
        try:
            user_number = int(input("Enter a number ({}-{})".format(lower, upper)))
            if user_number <= upper and user_number >= lower:
                is_valid = True
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a valid number!")

    return user_number


main()