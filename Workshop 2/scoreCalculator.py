"""This program takes a score from the user and
calculates its classification"""

score = float(input("Please enter score: "))
while score < 0 or score > 100:
    print("That is not a valid score.")
    score = float(input("Please enter score: "))

if score >= 90:
    print("Excellent!")
elif score >= 50:
    print("Passable")
else:
    print("BAD!")
