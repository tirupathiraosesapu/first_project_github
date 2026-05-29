# import calculations as cal
from packages.calculations import *
import random

"""print(cal.addition(10, 20))
print(cal.subtraction(20, 30))
print(cal.multiplication(5, 6))
print(cal.division(10, 2))

print(cal.students)"""

# print(addition(10, 20))
# print(subtraction(20, 30))
# print(multiplication(5, 6))
# print(division(10, 2))

# print(students)


characters = "ABCDEFGabcedfg123567890"

password = ""

for i in range(10):
    password += random.choice(characters)

print(password)