is_leap_year = False
input_year = int(input("Enter the year: "))

# Check if the input year is a century
if (input_year % 100 == 0):
    # Check if the input year is divisible by 400,if yes set leap year to true, if not set leap year to false
    if (input_year % 400 == 0):
        is_leap_year = True
    else:
        is_leap_year = False
else:
    # Check if the input year is divisible by 4,is yes set leap year to true, if not set leay year to false
    if (input_year % 4 == 0):
        is_leap_year = True
    else:
        is_leap_year = False

if is_leap_year == True:    
    print("{} - leap year".format(input_year))
else:
    print("{} not a leap year".format(input_year))
