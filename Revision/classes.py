class FirstClass:

    def __init__(self, name, age):
        # self.name = "TechU"
        # self.age = 30
        # self.Name = name
        # self.Age = age
        print("Function is called")

    # def normal(self):
    #     self.Name = "Python Full Stack"
    #     self.tech = "Django"

    # Methods
    def firstFunction(ramu):
        print("This is the first Function")

    def showDetails(raju):
        print(f"My name is {raju.Name} & my age is {raju.tech}")


"""obj1 = FirstClass()
obj2 = FirstClass()
obj3 = FirstClass()

print(obj1, type(obj1))

obj1.firstFunction()
print(obj1.name)
print(obj1.age)
obj1.name = "Innovations"
obj1.age = 40

print(obj1.name, obj2.name, obj3.name)
print(obj1.age)
"""

# person1 = FirstClass("Charan", 23)
# person2 = FirstClass("Kiran", 25)

# person1.Name = "Harish"
# print(person1.Name, person1.Age, type(person1))
# print(person2.Name, person2.Age, type(person2))
# person1.showDetails()
# person2.showDetails()


person2 = FirstClass()
person2.normal()
person2.showDetails()
