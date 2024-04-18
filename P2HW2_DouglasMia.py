#Mia Douglas
#03/10/2024
#P2HW2
#Create a program that askes the user fro their grades and averages them.

#Asks user for first grade
m1=float(input("Enter grade for module 1 : "))
#Asks user for second grade
m2=float(input("Enter grade for module 2 :"))
#Asks user for third grade
m3=float(input("Enter grade for module 3 :"))
#Asks user for fourth grade
m4=float(input("Enter grade for module 4 :"))
#Asks user for fifth grade
m5=float(input("Enter grade for module 5 :"))
#Asks user for sixth grade
m6=float(input("Enter grade for module 6  :"))

#grades empty list
grades=[ ]

#one by one grades into list with name grades
grades.append(m1)
grades.append(m2)
grades.append(m3)
grades.append(m4)
grades.append(m5)
grades.append(m6)

print("Grades list is: \n",grades)

lg=min(grades)
hg=max(grades)
sg=sum(grades)
avg=sg/6

#This prints the results
print("-----------------------------Results---------------------------")
print("Lowest grade :   ",lg)
print("Highest grade:   ",hg)
print("Sum of grades:   ",sg)
print("Average:       %.2f"%avg)

print("----------------------------------------------------------------")

