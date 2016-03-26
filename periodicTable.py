FILENAME = 'Periodic-Table.csv'


def main():
    periodic_file = open(FILENAME, 'r')
    row_list = get_useable_row(periodic_file)

    symbol_mass_dict = get_symbol_and_mass_dict(row_list)
    # print(symbol_mass_dict)
    formula = input("Please enter chemical formula separated by dashes (H2O = H2-O): ")
    symbols, quantities = parse_element(formula)
    total_mass = 0
    index_count = 0
    for symbol in symbols:
        # find the mass of the required symbol
        # multiply mass by required quantity
        # add new mass to total mass
        if quantities[index_count] == '':
            total_mass += symbol_mass_dict[symbol][0]
        else:
            total_mass += symbol_mass_dict[symbol][0] * int(quantities[index_count])
        index_count += 1
    print("The total atomic mass of {} is: {:<5.2f}".format(formula, total_mass))
    print("It is made up of: ")
    for symbol in symbols:
        print(symbol_mass_dict[symbol][1])


def get_useable_row(periodic_file):
    """Returns a list of rows of only the useful information from the periodic table file\
    periodic_file = CSV periodic table file"""
    row_list = []
    for line in periodic_file:
        line = line.strip()
        line_list = line.split(',')
        if not line_list[0].isnumeric():
            continue
        else:
            row_list.append(line_list[:8])
    return row_list


def get_symbol_and_mass_dict(row_list):
    """Returns a dict of just the element symbols and mass from a larger list of properties"""
    new_dict = {}
    for row in row_list:
        new_dict[row[1]] = [float(row[-2]), row[5]]
    return new_dict


def parse_element(input_string):
    symbol_list = []
    symbol_str = ''
    quantity_list = []
    quantity_str = ''

    element_list = input_string.split('-')
    for element in element_list:
        for char in element:
            if char.isalpha():
                symbol_str += char
            else:
                quantity_str += char
        symbol_list.append(symbol_str)
        quantity_list.append(quantity_str)
        symbol_str = ''
        quantity_str = ''

    return symbol_list, quantity_list


main()
