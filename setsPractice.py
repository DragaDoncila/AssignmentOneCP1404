"""1. Sets are collections, but they are not sequences i.e. it does not matter what order
the elements in a set are placed in, and they may not print in the order you assign
them. For this reason, sets are not indexable. Additionally, a set will only hold one of each
element, and any further elements added which are the same will not be added.

2. A sets 'in' operator returns a Boolean depending on whether or not the set being called
contains the element being checked. e.g. 2 in {1,2,3} returns True. {2, 4} in {2, 3, 4}
returns False.

3. Because the key is mapped to a value, changing it can mean you won't be able to access the
value before refinding the key. Could mean printing out the dictionary, or iterating through it.
If it's a large dictionary this could take literal hours"""

# Question 4
# dictionary_a = {'a': 3, 'x': 7, 'r': 5, 'j': 7}
# print(dictionary_a['x'])
#
# for key, value in dictionary_a.items():
#     if value == 7:
#         print(key)
#
# # Question 5
# other_hash = {}
# other_hash[2] = 10
#
# self_hash = {}
# self_hash[2] = other_hash
# print(self_hash)
# print(other_hash)
#
# self_hash[3] = 4
# print(self_hash)
# self_hash['2'] = self_hash
# # {2: {2:10}, 3: 4, '2': {2: {2:10}, 3: 4, '2': {.....}}
# # Because the dict within dict is recursive, indexing into '2' will only ever
# # return the dictionary itself, regardless of how many times you index into '2'.
# # It's only once you index into the dictionary itself, outside of the self-reference, that
# # you break the recursion.
# print(self_hash)
# print(self_hash["2"])
# print(self_hash['2']['2'])
# print(self_hash['2']['2']['2'])
# print(self_hash['2']['2']['2']['2']['2']['2']['2'][2][2])
#
# # Question 6
# list1 = ['Jane', 'John', 'Joe']
# list2 = ['Doe', 'Deer', 'Black']
# list3 = [23, 24, 50]
# # zip returns a tuple of the elements at the same index in the two (or more) lists
# dict_names = set(zip(list1, list2))
# print(dict_names)
#
# # Question 7
# """my_set = 'bcd', your_set = 'abcde'
# my_set.issubset(your_set) = True
# your_set.issubset(my_set) = False BUT your_set.issuperset(my_set) = True"""
# my_set = set('bcd')
# your_set = set('abcde')
# print(my_set.issubset(your_set))
# print(your_set.issuperset(my_set))
#
# # Question 8
my_dict = {'a':15, 'c':35, 'b': 20}
#
# for key in my_dict.keys():
#     print(key, end=" ")
#
# for value in my_dict.values():
#     print(value, end=" ")
#
# for key, value in my_dict.items():
#     print(key, ":", value, end=" ")

# get a list of tuples with the keys first, sorta that, dictionary it
my_dict_list =[]
for key, value in my_dict.items():
    my_dict_list.append((key, value))
my_dict_list.sort()
for element in my_dict_list:
    print(element)

my_dict_list = []
for key, value in my_dict.items():
    my_dict_list.append((value, key))
    my_dict_list.sort()
for element in my_dict_list:
    print(element)