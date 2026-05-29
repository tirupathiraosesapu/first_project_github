"""
(PascalCase)
class ClassName:
    statements
    variable
    functions

"""

class FirstClass:
    pass

"""
Object

object_name  = className()
object_name_1 = className()
"""

value1 = FirstClass()
value2 = FirstClass()

# -------------------------------
# Attributes(variables) and methods(functions) in OOp's concept

class SecondClass:
    def details(self):
        self.name = "Rehman"
        self.age = 25

student1 = SecondClass()
# print(student1)

student1.details()

# print(student1.name)
# print(student1.age)

student1.name = "Charan"
student1.age = 26
# print(student1.name)
# print(student1.age)

# ------------------------------------------
class ThirdClass:
    def details(self):
        print("This is inside the third class")

s1 = ThirdClass()

# s1.details()
# name = "welcome"

# -----------------------------------

class Student:
    def addDetails(self):
        """self.name = "Kiran"
        self.age = 30
        self.qualification = "B.tech"""
        self.name = input("Enter your Name : ")
        self.age = input("Enter your age")
        self.qualification = input("Enter your qualification : ")

    def showDetails(value):
        print(f"My name is {value.name}, age is {value.age} and my qualification is {value.qualification}")

std1 = Student()

# std1.addDetails()

# std1.showDetails()

# Student.addDetails()
# Student.showDetails()

# -----------------------------------
# Constructor

class Constructor:
    def __init__(self):
        print("This is comes from the constructor")


# v1 = Constructor()
# v2 = Constructor()


class Car:
    def __init__(self, fullName):
        self.name = fullName
        # print("Car name is", fullName)
    
    def details(self):
        print(self.name)

    # def 

# car1 = Car("BMW")
# car2 = Car("Audi")
# car3 = Car("Benz")

# car1.details()

# -----------------------------------

class StudentDetails:
    def __init__(self, firstName, lastName, age, qualification, city, mobile):
        self.first_name = firstName
        self.last_name = lastName
        self.age = age
        self.qualification = qualification
        self.city = city
        self.mobile = mobile

    def showDetails(this):
        print(f"My Full name is : {this.first_name} {this.last_name}\nMy age is : {this.age}\nMy qualification is : {this.qualification}\nCity : {this.city}\nMobile : {this.mobile}")

m1 = StudentDetails("Charan", "Kumar", 25, "B.tech", "Hyderabad", 1234567890)
m2 = StudentDetails("Surya", "Surya", 24, "Degree", "Kurnool", 987654321)


m1.showDetails()
print("----------------------")
m2.showDetails()









