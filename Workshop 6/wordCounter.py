"""Get a string from the user and count unique words"""

text = input("Text: ")
words = text.lower().split()
word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1
#     OR
#         ""Gets the word in word counts if it exists, if not sets to 0
#      word_counts[word] = word_counts.get(word, 0) + 1

for word, count in sorted(word_counts.items()):
    print("{:10s} : {:3d}".format(word, count))