FILENAME = "numbers.txt"

numbers_file = open(FILENAME, "r")
sum_num = 0
for line in numbers_file:
    sum_num += int(line.strip())

print(sum_num)

numbers_file.close()
