LOWER = 33
UPPER = 127

ascii_code = input(("Enter a number ({}-{}): ".format(LOWER, UPPER))).strip()
# print(ascii_code)
for i in range(LOWER,UPPER):
    print("{:>5}{:>8}".format(i, chr(i)))