def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Read the year from the user
year = int(input("Enter a year: "))

# Check if it's a leap year and print the result
print(is_leap(year))
