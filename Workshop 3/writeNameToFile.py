FILENAME = "data.txt"

name = input("Please enter your name: ")
name_file = open(FILENAME, "w")
# print(name, file=name_file)
name_file.write(name)

name_file.close()
