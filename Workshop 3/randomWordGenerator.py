import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = input("Create a word! Type @ for a consonant, # for a vowel, all other letters stay put!: ").lower()
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
    else:
        word += kind
print(word)