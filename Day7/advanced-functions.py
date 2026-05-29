def welcomeUser(name, age, location="Hyderabad"):
    return f"My name is {name}, {age} years old and from {location}"


value = welcomeUser("Tirupathi", 27, "Vijayawada")
# print(value)
value1 = welcomeUser("Surya", 24)
# print(value1)

value2 = welcomeUser(location="Karnool", age=20, name="Kiran") #Keyword arguments
# print(value2)

# value3 = welcomeUser(location="Hyderabad", 30, "welcome")

# def welcomeNote(location="Vijayawada", name, age):
#     pass


def addition(a, b, c, d):
    return a+b+c+d

# print(addition(1, 2, 3, 4))

def summation(*a):
    return sum(a)

# print(summation(1, 2))
# print(summation(1, 2, 3))
# print(summation(1, 2, 3, 4))


def length(*values):
    print(values, type(values))
    for value in values:
        print(value, type(value))
    # print(max(values))

# length(10, 22, 44, 13)
# length(10, 20, "40", 66)



def studentInformation(name, age, location="Hyderabad", *marks):
    print(f"My name is {name}, {age} years old and from {location} and my final marks is {sum(marks)}")


# studentInformation("Surya", 22, "Warangal", 10, 20, 30, 40, 50)
# studentInformation("Vamshi", 24, 10, 20, 30, 40, 50)
# studentInformation("Kiran", 24, "Srikakulam", 10, 20, 30, 40, 50)

# ---------------------------------

def multipleKeywordArguments(**values):
    print(values, type(values))
    for key, value in values.items():
        print(key, f"{type(key)} =>{type(value)} ", value)
    

# multipleKeywordArguments(name="Tirupathi", age=20, number= 1234567890)



def allFunctionCombination(name, age, location="Hyderabad", *marks, **information):
    print(f"My name is {name}, {age} years old and from {location} and my final marks is {sum(marks)}")
    for key, values in information.items():
        print(key, values)


allFunctionCombination("Manisha", 22, "Secunderabad", 20, 45, 66, address="23-36-10/2", number=123567890, qualification="B.Tech")