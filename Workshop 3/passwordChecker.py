MIN_LENGTH = 2
MAX_LENGTH = 8
REQUIRES_CHARACTER = True
CHARACTER_STRING = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"
PASSWORD_STRING = """Your password must be between {} and {} characters.
It must contain 1 or more uppercase characters
It must contain 1 or more lowercase characters
It must contain 1 or more numbers
It must contain 1 or more special characters""".format(MIN_LENGTH, MAX_LENGTH)

print(PASSWORD_STRING)
potential_password = input(">>>")

is_valid = False
count_lowers = 0
count_uppers = 0
count_nums = 0
count_chars = 0
while not is_valid:
    if len(potential_password) < MIN_LENGTH or len(potential_password) > MAX_LENGTH:
        print("Invalid password!")
        potential_password = input(">>>")
    for char in potential_password:
        if char.lower() == char:
            count_lowers += 1
        if char.upper() == char:
            count_uppers += 1
        if char.isnumeric():
            count_nums += 1
        if char in CHARACTER_STRING:
            count_chars += 1
    if count_lowers > 0 and count_uppers > 0 and count_nums > 0 and count_chars > 0:
        is_valid = True
    else:
        print("Invalid password!")
        potential_password = input(">>>")
print("Your {} character password is valid: {}".format(len(potential_password), potential_password))

