from guitar import Guitar

print("My guitars!")

name = input("Name: ")
# guitars made list literal
guitars = list()
# while name != "":
#     year = int(input("Year: "))
#     cost = float(input("Cost: $"))
#     new_guitar = Guitar(name, year, cost)
#     guitars.append(new_guitar)
#     print(new_guitar, 'added')
#     name = input("Name: ")
guitars.append(Guitar("Black", 2010, 56000))
guitars.append(Guitar("Blue", 1960, 2000))
guitars.append(Guitar("Pink", 1920, 500))
print(" "*10, "... snip ...")
print("These are my guitars!")
count = 1
for guitar in guitars:
    print("Guitar {}: {:20s}, worth ${:10,.2f} {}".format(
        count, guitar.name + "(" + str(guitar.year) + ")", guitar.cost, '(vintage)' if guitar.is_vintage() else ""
    ))
# line at end added
