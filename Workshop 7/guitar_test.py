from guitar import Guitar

my_guitar = Guitar("Fender Stratocaster", 1954, 25000)

print(my_guitar)
print(my_guitar.get_age())
print("This guitar is vintage: {}".format(my_guitar.is_vintage()))