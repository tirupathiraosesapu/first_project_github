class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def documentation(self):
        print("Trainer Documentation")
    
    def exampleCode(self):
        print("Live session coding")


class Surya(Teacher):       #parent is Teacher
    def __init__(self,name, age, qualification):
        super().__init__(name, age)
        self.qualification = qualification

    def classBunk(self):
        print(f"My name is {self.name} & age is {self.age} and qualification is {self.qualification}")

class Manisha(Teacher):
    def showDetails(self):
        print(f"My name is {self.name} and myh age is {self.age}")

class Charan(Surya):    # parent is Surya
    def __init__(self, name, age, qualification, address):
        super().__init__(name, age, qualification)
        self.address = address

    def showDetails(self):
        print(f"My name is {self.name} & age is {self.age} and qualification is {self.qualification} and my address is {self.address}")

t1 = Teacher("Tirupathi", 25)
print(t1.name, "--", t1.age)
t1.documentation()
t1.exampleCode()
# t1.classBunk()
print("-----------------------------")

s1 = Surya("Surya", 22, "B.tech")
print(s1.name, "--", s1.age)
s1.documentation()
s1.exampleCode()
s1.classBunk()
print("-----------------------------")

m1 = Manisha("Manisha", 23)
print(m1.name, "--", m1.age)
m1.documentation()
m1.exampleCode()
m1.showDetails()
# m1.classBunk()

print("-----------------------")

c1 = Charan("Charan", 26, "Degree", "address")
print(c1.name, "--", c1.age, "--", c1.qualification, "--", c1.address)
c1.documentation()
c1.classBunk()
c1.exampleCode()
c1.showDetails()