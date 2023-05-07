import random

# Line 1
random_number1 = random.randint(5, 20)
print(random_number1)
# The output will be a random integer between 5 and 20 (inclusive)
# The smallest number that could be seen is 5 and the largest is 20.

# Line 2
random_number2 = random.randrange(3, 10, 2)
print(random_number2)
# The output will be a random odd integer between 3 and 9 (inclusive)
# The smallest number that could be seen is 3 and the largest is 9.
# No, line 2 could not have produced a 4 because the step value is 2, so only odd numbers will be generated.

# Line 3
random_number3 = random.uniform(2.5, 5.5)
print(random_number3)
# The output will be a random float between 2.5 and 5.5 (inclusive)
# The smallest number that could be seen is 2.5 and the largest is 5.5.

# Random number between 1 and 100 (inclusive)
random_number4 = random.randint(1, 100)
print(random_number4)
# The output will be a random integer between 1 and 100 (inclusive)