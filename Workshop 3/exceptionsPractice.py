try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    print("Finished.")

# A ValueError will occur when the user's inputs are not valid integers
# A ZeroDivisionError will occur when 0 is entered as the denominator. Classical maths does not allow for 0 division.
# You could check that the denominator is greater than 0 before attempting the fraction
