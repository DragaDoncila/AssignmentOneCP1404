"""This program gets a users name, displays a menu and allows
user to make choices until quit is selected"""
MENU = """(H)ello
(G)oodbye
(Q)uit"""

name = input("Enter name: ")

print(MENU)
choice = input(">>>").lower()
while choice != "q":
    if choice == "h":
        print("Hello,", name)
    elif choice == "g":
        print("Goodbye,", name)
    else:
        print("This is not a valid choice,", name)
    print(MENU)
    choice = input(">>>").lower()
print("Finished.")
