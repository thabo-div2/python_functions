# Exercise 1 - Python Functions

# Defining an argument
def distance_from_zero(x):
    # Passing an argument
    if type(x) == int or type(x) == float:  # Checking the type of variants
        return abs(x)
    else:
        return "Nope"


print(distance_from_zero(-5))
print(distance_from_zero(6))
print(distance_from_zero("what?"))

# Exercise 2


def is_leap(year):
    leap = False
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True

    return leap


year = int(input("Enter the year: "))

print(is_leap(year))
