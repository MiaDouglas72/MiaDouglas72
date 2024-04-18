#Mia Douglas
#03/24/2024
#P3HW2
#Program displays the following Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay

# Get employee's name
employee_name = input("Enter the name of the employee: ")

# Get number of hours worked
hours_worked = float(input("Enter the number of hours worked this week: "))

# Get employee's pay rate
pay_rate = float(input("Enter the employee's pay rate: "))

# Check for overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display the results
print("Employee Name:", employee_name)
print("Pay Rate:", pay_rate)
print("Number of Hours Worked:", hours_worked)
print("Overtime Hours:", overtime_hours)
print("Overtime Pay:", overtime_pay)
print("Pay for Regular Hours:", regular_pay)
print("Gross Pay:", gross_pay)
