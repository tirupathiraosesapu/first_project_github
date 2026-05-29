# print("Welcome to the Python Class")

for i in range(5):
    # print("Welcome to the Python Class")
    pass

"""
def function_name():
    statement
"""
# firstFunction()
def firstFunction():
    print("THis is comes from functions")

# firstFunction()

# firstFunction()


def add():
    print(10+20)

# add()
# add()

# ---------------------------------

def welcomeNote(name, age):
    # print(f"My name is {name} and I'm {age} years old")
    return f"My name is {name} and I'm {age} years old"

# welcomeNote("Rehman", 26)
# welcomeNote("Surya", 22)


def multiplication(a, b):
    print(a*b)

multiplication(10, 20)

value = multiplication(20, 5)
# print(value)
# print(value)

def division(a,b):
    # print("WElcome")
    return a//b
    

# print(division(10, 2))

second_value = division(25, 4)
# print(second_value)


def student(name, age):
    print(name, age, sep="\n")

# student("Manisha", 22)


def loginUser(username, password):
    if username=="Surya" and password=="1234":
        print("Login Successfull")
    else:
        return "Please enter valid credentials"

loginUser("1234", "Surya")
# loginUser(password="1234", username="Surya") 