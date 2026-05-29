# Condiitons in Python

# if condiiton

"""
if condition:
    statement


"""

"""if True:
    print("This is the block of code")
    print("WElcome")"""

age = 20

"""if age>18:
    print("You are eligible for the voting")
else:
    print("You are not eligible")"""
    
full_name = "TechU"

# print(len(full_name))

marks =52

"""if marks >=90:
    print("A grade")
elif marks >=75 and marks <90:
    print("B grade")
elif marks >=50 and marks <75:
    print("C grade")
else:
    print("Failed")"""


age = 18
is_active = True


"""if age>18:
    # print("You are eligible")
    if is_active:
        print("Your status is active")
    else:
        print("Your status is inactive")
else:
    print("You are not eligible")"""


username = "Tirupathi"
password = "12345"

input_user = input("Enter your user name :")
input_password = input("Enter your password :")

if username==input_user:
    if input_password == password:
        print("Login Success")
    else:
        print("Password in wrong")
else :
    print("User name is wrong")