"""
CP1404/CP5632 Workshop 05
CSV scores file program - broken one
scores file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
"""

__author__ = 'Lindsay Ward'

scores_file = open("scores.csv")
scores_data = scores_file.readlines()
print(scores_data)
for element in scores_data:
    element = element.strip()
subjects = scores_data[0].strip().split(",")

print(subjects)
# subject_scores = [[] for subject in subjects]
# score_values = []
# for score_line in scores_data[1:]:
#     score_strings = score_line.strip().split(",")
#     score_numbers = [int(value) for value in score_strings] #all the numbers in columns
#     for index in range(len(score_numbers)):
#         subject_scores[index].append(score_numbers[index])
#     # score_values.append(score_numbers[count])
#     # print(score_values)
#     print(score_numbers)

scores_file.close()

# for i in range(len(subjects)):
#     print(subjects[i], "Scores:")
#     for score in score_values[i]:
#         print(score)
#     print("Max:", max(score_values[i]))
#     print()
