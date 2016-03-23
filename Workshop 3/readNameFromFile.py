FILENAME = "data.txt"

name_file = open(FILENAME, "r")
name = name_file.readline().strip()
print("Your name is {}".format(name))

name_file.close()