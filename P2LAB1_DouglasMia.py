# Mia Douglas
# 03/03/2024
# P2LAB1
# Write a program with a car's gas mileage and the cost of gas as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles


miles_per_gallon = float(input("Enter the car's gas mileage (miles/gallon): "))
dollars_per_gallon = float(input("Enter the cost of gas (dollars/gallon): "))


your_value1 = (20 / miles_per_gallon) * dollars_per_gallon
your_value2 = (75 / miles_per_gallon) * dollars_per_gallon
your_value3 = (500 / miles_per_gallon) * dollars_per_gallon


print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')
