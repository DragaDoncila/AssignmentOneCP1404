FILENAME = 'items.csv'
MENU = """Menu:
(L)ist all items
(H)ire an item
(R)eturn an item
(A)dd new item to stock
(Q)uit"""

def main():
    items_file = open(FILENAME, 'r')
    all_items = generate_list_from_file(items_file)
    print(MENU)
    menu_choice = get_valid_choice()

    while menu_choice != 'q':
        if menu_choice == 'l':
#             TODO: write display list
            print(MENU)
            menu_choice = get_valid_choice()
        elif menu_choice  == 'h':
#             TODO: write hire_item
            print(MENU)
            menu_choice = get_valid_choice()
        elif menu_choice == 'r':
#             TODO: write return_item
            print(MENU)
            menu_choice = get_valid_choice()
        elif menu_choice == 'a':
#             TODO: write add_item
            print(MENU)
            menu_choice = get_valid_choice()

#   TODO: write to file
    print("Goodbye")
    items_file.close()

def generate_list_from_file(file):
    all_items = []

    for line in file:
        properties_list = line.strip().split(",")
        all_items.append(properties_list)

    return all_items

def get_valid_choice():
    choice = input(">>> ").lower()
    valid_options = 'lhraq'

    while choice not in valid_options:
        print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").lower()

    return choice

main()