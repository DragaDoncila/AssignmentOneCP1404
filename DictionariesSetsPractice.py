# contacts = {'bill': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}
# # print(contacts)
# # print(contacts['bill'])
# # print(contacts['jane'])
# # contacts['barb'] = '271-1234'
# # print(contacts)
#
# demo = {2: ['a', 'b', 'c'], (2,4): 27, 'x': {6: 2.5, 'a':3}}
# # print(demo)
# # print(demo[2])
# # print(demo[(2,4)])
# # print(demo['x'])
# # print(demo[2][0]) #indexing a list means you index by position, indexing into a dict you index by key
# print(len(demo))
# print(2 in demo)
# print(1 in demo)
# for key in demo:
#     print(key, end=" ")

# for key in demo:
#     print('\n',key, demo[key])
# print(min(demo))

# my_dict = {'a': 2, 3: ['x', 'y'], 'joe': 'smith'}
# for key, val in my_dict.items():
#     print("Key: {:<7} Value: {}".format(key, val))
#
# my_dict_values = my_dict.values()
# print(my_dict_values)
# for val in my_dict_values:
#     print(val, type(val))

word_list = ['the', 'black', 'and', 'the', 'black', 'the', 'and', 'black', 'and', 'and', 'and']
word_dict = {}
for word in word_list:
    word_dict[word] = word_dict.get(word, 0) + 1
print(word_dict)

last_biggest_val = 0
last_biggest_word = ''
# for word in word_dict:
#     if word_dict[word] > last_biggest_val:
#         last_biggest_word = word
#         last_biggest_val = word_dict[word]
# print(word_dict[last_biggest_word])
for word,frequency in word_dict.items():
    if frequency > last_biggest_val:
        last_biggest_word = word
        last_biggest_val = frequency
print(last_biggest_word)
