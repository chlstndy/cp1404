"""
1. It will occur when the wrong value is assigned to an object, e.g. invalid value for a given operation or value
that does not exist.
2. It will occur when a number is attempted to be divided by zero.
3. Yes, by using a conditional statement to check for a denominator or divisor of 0 before performing the operation.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
