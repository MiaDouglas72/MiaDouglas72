# Mia Douglas
# 03/10/2024
# P2HW1
# Create a program that does some basic math on numbers that are entered.


print(f"This program calculates and displays travel expenses")
#this prompts the user to enter a budget 
budget = input("Enter budget:\n")
#this prompts user to enter the desination
travel_destination = input("Enter your travel destination:\n")
#this prompts user to enter estimated amount spent on fuel
fuel = input("How much do you think you will spend on gas?:\n")
#this prompts user to enter estimated amount sent on the hotel
accomodation = input("Approximately, how much will you need for accomodation/hotel?:\n")
#this prompts user to enter estimated amount spent on food
food = input("Last, how much do you need for food?:\n")

#this prints the budget report
print("--------Travel Expenses--------")
print(f"Location: {travel_destination}")
print(f"Initial Budget:  ${budget}")
print(f"Fuel:  ${fuel}")
print(f"Accomodation:  ${accomodation}")
print(f"Food:  ${food}")
#this prints the total amount left over
remaining_balance = int(budget) - int(fuel) - int(accomodation) - int(food)
print(f"Remaing Balance:  ${remaining_balance}")
