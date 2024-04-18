# Mia Douglas
# 04/04/2024
# P4LAB2
# Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.

# Get input integers
first_integer = int(input())
second_integer = int(input())

# Check if the second integer is less than the first
if second_integer < first_integer:
    print("Second integer can't be less than the first.")
else:
    # Output the sequence with an increment of 5
    current_value = first_integer
    while current_value <= second_integer:
        print(current_value, end=' ')
        current_value += 5
