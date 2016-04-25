"""Practice with defining and using classes, as well as exercises from textbook Ch. 11 (Practice of Computing)
Ch. 11 (Starting out With Python)"""

"""The __init__ method is a method which would run regardless of our defining it, as it is the "constructor" of our
instance. By redefining it from default, we can construct the instance (straight away) with defined attributes (default
or otherwise specified) and their values, in the "class call" i.e. when we first define the instance. In other words we
pass arguments into the parameters we define for __init__ which will act as the value of that instance's attributes"""


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

    def return_kooky_string(self):
        return "The {} {} used its {} legs to jump high!".format(self.colour, self.species, self.num_legs + 6)

    def change_numlegs(self, num_legs):
        self.num_legs = num_legs


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


"""Table Fan class:
    attributes: name, num_speeds, is_oscillating, manufacturer, cost, cord_length, wattage
    methods: __str__, set_speed, toggle_oscillation,"""


class TableFan(object):
    def __init__(self, name="", manufacturer="", cost=0, cord_length=0, wattage=0,
                 num_speeds=1, can_oscillate=False):
        self.name = name
        self.manufacturer = manufacturer
        self.cost = cost
        self.cord_length = cord_length
        self.wattage = wattage
        self.num_speeds = num_speeds
        self.can_oscillate = can_oscillate

        self.__current_speed__ = 1
        self.__is_oscillating__ = False


    def set_speed(self, speed_setting):
        if speed_setting > self.num_speeds or speed_setting < 0:
            print("Invalid speed setting. Attribute not set")
        else:
            self.__current_speed__ = speed_setting

    def set_oscillation(self, oscillation):
        if not self.can_oscillate:
            print("Nah bitch")
            return

        if oscillation != 0 and oscillation != 1:
            print("Invalid oscillation state")
        else:
            if oscillation == 0:
                self.__is_oscillating__ = False
            else:
                self.__is_oscillating__ = True

    def compare_cost(self, other_fan):
        if self.cost > other_fan.cost:
            print("Your fan is cheaper")
        elif self.cost < other_fan.cost:
            print("{} is cheaper".format(other_fan.name))
        else:
            print("Same price")

    def display_state(self):
        title_str = '{:20s} {:20s} {:20s} \n'.format('Name', 'Current Speed', 'Oscillation State')
        if not self.can_oscillate:
            oscillation_state = 'N/A'
        else:
            if self.__is_oscillating__:
                oscillation_state = 'On'
            else:
                oscillation_state = 'Off'
        state_str = '{:20s} {:20s} {:20s}'.format(self.name, str(self.__current_speed__), oscillation_state)
        return title_str + state_str

    def __str__(self):
        title_str = "{:20s} {:20s} {:20s} {:20s} {:20s} {:20s} {:20s}\n".format(
            "Name", "Manufacturer", "Cost", "Wattage", "Cord Length", "Speeds", "Oscillation")
        value_str = "{:20s} {:20s} {:20s} {:20s} {:20s} {:20s} {:20s}".format(
            self.name, self.manufacturer, str(self.cost), str(self.wattage), str(self.cord_length),
            str(self.num_speeds), str(self.can_oscillate))
        return title_str + value_str


"""Album class:
    attributes: name, artist, year, length, numtracks, tracklisting (as tuple?)
    methods: __str__, """


class Pet:

    def __init__(self, name="", species="", age=0):
        self.__name = name
        self.__species = species
        self.__age = age

    def set_name(self, new_name):
        self.__name = new_name

    def set_species(self, new_species):
        self.__species = new_species

    def set_age(self, new_age):
        self.__age = new_age

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age


class Car:
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def __str__(self):
        return '{} {}'.format(self.__make, self.__year_model)







# stu1 = Student("Terry", "Hatchett", 3596)
# print(stu1)
#
# animal1 = Animal("kitteh", "black", 4)
# print(animal1)
#
# mycart = ShoppingCart(4, 25, [5, 36.23, 134.50, 34.60])
# print(mycart)
# mycart.clear_cart()
# mycart.add_item(35)
# mycart.add_item(46)
# mycart.add_item(235)
# print(mycart)
# horse = Animal('equine', 'pink', 4)
# print(horse)
# print(horse.return_kooky_string())
# num_legs = int(input("What's the new number of legs?"))
# horse.change_numlegs(num_legs)
# # horse.num_legs = 10
# print(horse.return_kooky_string())

# new_fan = TableFan("Turbonator", "Panasonic", 200, 5, 400, 5, True)
# print(new_fan)
# new_fan.set_oscillation(1)
# new_fan.set_speed(6)
# print(new_fan.display_state())
# new_fan.set_speed(3)
# print(new_fan.display_state())
# other_fan = TableFan("Turbo+", "Hitachi", 230, 2, 600, 6, True)
# print(other_fan)
# new_fan.compare_cost(other_fan)
# new_fan.compare_cost(new_fan)
# other_fan.set_speed(7)
# other_fan.set_oscillation(1)
# print(other_fan.display_state())

# myPet = Pet()
# pet_name = input("Pet's Name: ")
# pet_species = input("Pet's Species: ")
# pet_age = int(input("Pet's Age: "))
# myPet.set_name(pet_name)
# myPet.set_species(pet_species)
# myPet.set_age(pet_age)
#
# print("{} is the loveliest {} year old {} I've ever seen!".format(myPet.get_name(), myPet.get_age() ,
# myPet.get_species()))

# myCar = Car(2000, "Masseratti")
# for i in range(5):
#     myCar.accelerate()
#     print("{}'s current speed is {}".format(myCar, myCar.get_speed()))
# print()
# for j in range(5):
#     myCar.brake()
#     print("{}'s current speed is {}".format(myCar, myCar.get_speed()))

