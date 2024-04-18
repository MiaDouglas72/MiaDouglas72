# Mia Douglas
# 03/03/2024
# P2LAB2
#

a = float(input("Enter integer 1:"))
b = float(input("Enter integer 2:"))
c = float(input("Enter integer 3:"))
d = float(input("Enter integer 4:"))

avg = (a + b + c + d) / 4

product = a * b * c * d

print('{:.0f} {:.0f}'.format(round(product),round(avg)))
print('{:.3f} {:.3f}'.format(product,avg))
