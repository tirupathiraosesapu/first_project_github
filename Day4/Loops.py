# While loop

"""
while condition:
    statement
    increment
"""
# Basic counting
"""i = 16

while i<=20:
    print(i)
    i+=1"""

# reverse counting
"""j = 20

while j>0:
    print(j)
    j-=1"""

# Sum fo the numbers
"""num = 1 #increment
total = 0
while num<=10:
    total+=num
    num+=1
print(total)"""


# User input loop

"""num = 0

while num !=5:
    num = int(input("Enter 5 number to stop the loop : "))"""


# -------------------------------------
# for loop

"""
for variable in sequence:
    statement
"""

"""for x in range(10):
    print(x)
"""

"""for y in range(10, 20):
    print(y)"""

"""for z in range(1, 10, 5):
    print(z)
"""

"""for ch in "Python Full Stack":
    print(ch, sep=" ", end="")"""

# ----------------------------------
# break statement


"""for value in range(10):
    if value == 5:
        break
    print(value)"""



"""for value in range(10):
    if value%2 != 0:
        continue
    print(value)"""
    
"""attempts = 0

while attempts<3:
    password = input("Enter your password")
    if password == "Tirupathi":
        print("Your are logged in")
        break
    else:
        print("Invalid password")
    attempts+=1"""


"""password = input("Enter your password : ")
while password != "Tirupathi":
    password = input("Enter your password : ")"""


"""for i in range(1, 20):
    if i == 5:
        pass
    print(i)"""

# nested loops

"""
1   1
1   2
2   1
2   2
"""

"""for row in range(1, 11):
    for column in range(1, 6):
        # print(row, column)
        print(row*column)"""


"""for row in range(5):
    for column in range(5):
        print("*", end=" ")
    print()"""


"""for value in "ABCD":
    for cha in "12345":
        print(value, cha)"""

# !5 => 5*4*3*2*1