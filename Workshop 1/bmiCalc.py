"""Draga Doncila, CP1404, 2016"""

print("Body Mass Index Calculator")

weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in metres: "))

bmi = weight / height ** 2

print("Therefore your BMI is:", bmi, "\nThank You!")
