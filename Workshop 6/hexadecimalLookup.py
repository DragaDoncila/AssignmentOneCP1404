# STATE_NAMES = {"QLD":"Queensland", "NSW": "New South Wales", "NT":"Northern Territory",
# "WA":"Western Australia", "ACT":"Australian Capital Territory", "VIC":"Victoria",
# "TAS":"Tasmania"}
#
# # print(STATE_NAMES)
#
# state = input("Enter short state: ").upper()
# while state != "":
#     if state in STATE_NAMES:
#         print(state, "is", STATE_NAMES[state])
#     else:
#         print("Invalid short state")
#     state = input("Enter short state: ").upper()

# HEXADECIMAL_COLOURS = {"AliceBlue": 'f0f8ff', "BlanchedAlmond": 'ffebcd', "chartreuse4": '458b00',
#                        "DimGray": '696969', "firebrick": 'b22222', "GreenYellow": 'adff2f',
#                        "LawnGreen": '7cfc00', "moccasin": 'ffe4b5'}
#
# colour = input("Enter a colour name: ")
# while colour != '':
#     if colour in HEXADECIMAL_COLOURS:
#         print("{} is the hexadecimal code {}".format(colour, HEXADECIMAL_COLOURS[colour]))
#     else:
#         print("That colour name is not recognized")
#     colour = input("Enter a colour name: ")


def new_func(value1 = 0, value2 = 1, value3 = 2):
    print(value1, value2, value3)

new_func(5,value3=10, value2=50)