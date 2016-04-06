class Student(object):

    def __init__(self, first="", last="", id_num=0):
        self.first_name = first
        self.last_name = last
        self.id = id_num

    def __str__(self):
        return '{} {}, ID: {}'.format(self.first_name, self.last_name, self.id)


class Animal(object):

    def __init__(self, species="", colour="", num_legs=0):
        self.species = species
        self.colour = colour
        self.num_legs = num_legs

    def __str__(self):
        return "The {} {} used its {} legs to jump high!".format(self.colour, self.species, self.num_legs)


class ShoppingCart(object):

    def __init__(self, num_items=0, time_to_expiry=30, item_costs=[]):
        self.num_items = num_items
        self.time_to_expiry = time_to_expiry
        self.item_costs = item_costs

    def clear_cart(self):
        self.num_items = 0
        self.time_to_expiry = 0
        self.item_costs.clear()

    def add_item(self, cost):
        self.num_items += 1
        self.item_costs.append(cost)
        self.time_to_expiry = 30

    def __str__(self):
        return "There are {} items in your cart, which will expire in {} minutes.\
                \nThe total cost of the items is ${:.2f}".format(
            self.num_items, self.time_to_expiry, sum(self.item_costs))

stu1 = Student("Terry", "Hatchett", 3596)
print(stu1)

animal1 = Animal("kitteh", "black", 4)
print(animal1)

mycart = ShoppingCart(4, 25, [5, 36.23, 134.50, 34.60])
print(mycart)
mycart.clear_cart()
mycart.add_item(35)
mycart.add_item(46)
mycart.add_item(235)
print(mycart)
