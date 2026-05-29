class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def animalSound(self):
        print("All animal sounds")
    
    def showDetails(self):
        print(f"My name is {self.name} and age is {self.age}")


class Cat(Animal):
    # pass
    def animalSound(self):
        print("Cat sound like Meow")

a1 = Animal("Cat", 2)
a1.animalSound()
a1.showDetails()

c1 = Cat("Dog", 5)
c1.animalSound()
c1.showDetails()