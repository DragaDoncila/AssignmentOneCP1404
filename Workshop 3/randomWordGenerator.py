import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def is_valid_format(word_format):
    for char in word_format:
        if char not in "@#":
            return False
    return True

word_format = input("Create a word! Type @ for a consonant, # for a vowel").lower()
while not is_valid_format(word_format):
    word_format = input("Create a word! Type @ for a consonant, # for a vowel").lower()
# word_format = ""
# for i in range(random.randint(6,12)):
#     word_format += random.choice("@#$")

word = ""
for kind in word_format:
    if kind == "@":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    # elif kind == "$":
    #     word += random.choice(VOWELS + CONSONANTS)
    # else:
    #     word += kind
print(word)