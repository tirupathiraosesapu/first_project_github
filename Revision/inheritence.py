class Tirupathi:
    def __init__(self, name, age, qualification):
        self.name = name
        self.age = age
        self.qualification = qualification

    def showDetails(self):
        print(
            f"My name is {self.name}, age is {self.age} and my qualification is {self.qualification}"
        )


"""c1 = Tirupathi("Charan", 25, "B.Tech")
c2 = Tirupathi("Surya", 24, "Degree")
c3 = Tirupathi("Kiran", 30, "MBA")

c1.showDetails()
c2.showDetails()
c3.showDetails()"""

"""
class Charan(Tirupathi):
    def __init__(self, name, age, qualification, course):
        super().__init__(name, age, qualification)
        self.course = course

    def welcome(self):
        super().showDetails()
        print("This is from charan class")

    def showDetails(self):
        print("This si from Charan Class")


class Surya(Tirupathi):
    pass


class Kiran(Charan):
    pass


p1 = Charan("Charan", 25, "B.Tech", "PFS")
p2 = Surya("Surya", 24, "Degree")"""
# p3 = Kiran("Kiran", 30, "MBA")

# p1.showDetails()
# print(p1.name)

# p3.welcome()


# p1.welcome()
# p1.showDetails()
# p2.showDetails()


class ATM:
    def __init__(self):
        self._atm = 1234
        self.__balance = 0

    # getters
    def showBalance(self):
        print(f"Your balance is {self.__balance}")

    # setters
    def deposite(self, amount):
        self.__balance += amount


person1 = ATM()

print(person1._atm)
# print(person1._balance)
person1.showBalance()
person1.deposite(500)
person1.showBalance()
