import random

CHARACTER_STRING = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"
UPPERCASE_STRING = "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
LOWERCASE_STRING = UPPERCASE_STRING.lower()
NUMERIC_STRING = "1234567890"

# min_length = int(input("Min length: "))
# max_length = int(input("Max length: "))
password_length = int(input("What is your password length: "))
uppercase_flag = input("Does it require uppercase letters (Y/N): ").lower()
lowercase_flag = input("Does it require lowercase letters (Y/N): ").lower()
number_flag = input("Does it require a number (Y/N): ").lower()
character_flag = input("Does it require a special character (Y/N): ").lower()

while uppercase_flag == "n" and lowercase_flag == "n" and number_flag == "n" and character_flag == "n":
    print("You think you're really clever don't'cha!")
    password_length = int(input("What is your password length: "))
    uppercase_flag = input("Does it require uppercase letters (Y/N): ").lower()
    lowercase_flag = input("Does it require lowercase letters (Y/N): ").lower()
    number_flag = input("Does it require a number (Y/N): ").lower()
    character_flag = input("Does it require a special character (Y/N): ").lower()

has_lower = False
has_upper = False
has_number = False
has_character = False

if uppercase_flag == "n":
    has_upper = True
if lowercase_flag == "n":
    has_lower = True
if number_flag == "n":
    has_number = True
if character_flag == "n":
    has_character = True
    # while password doesn't contain requirements
    #   iterate through 1- password length+1
    #         kind = random choice of kind
    #         if kind.....

while not has_lower or not has_upper or not has_number or not has_character:
    has_lower = False
    has_upper = False
    has_number = False
    has_character = False
    password = ""
    for i in range(password_length):
        # decides whether character will be (l)ower (u)pper (n)umber or (c)haracter
        kind = random.choice("lunc")
        if kind == "l":
            password += random.choice(LOWERCASE_STRING)
            has_lower = True
        elif kind == "u":
            password += random.choice(UPPERCASE_STRING)
            has_upper = True
        elif kind == "n":
            password += random.choice(NUMERIC_STRING)
            has_number = True
        elif kind == "c":
            password += random.choice(CHARACTER_STRING)
            has_character = True

print("Your password is: {}".format(password))
