# Mia Douglas
# 04/04/2024
# P5LAB
# Leap Year Functions

# Define the function
def days_in_feb(user_year):
    # Check if the year is a leap year
    if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        return 29  # Leap year: February has 29 days
    else:
        return 28  # Non-leap year: February has 28 days


if __name__ == "__main__":
    # Get input from the user
    user_year = int(input())

    # Call the function and display the result
    result = days_in_feb(user_year)
    print(f"{user_year} has {result} days in February.")
