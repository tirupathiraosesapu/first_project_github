from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self):
        self.name = "Tirupathi"
        self.age = 27

    @abstractmethod
    def login(self):
        print("This is the login page from parent")

    def logout(self):
        print("This is the logout page")


class Admin(User):
    def login(self):
        print("This is the login page from Admin")


class Trainer(User):
    pass


person1 = Admin()
person1.login()
person1.logout()


person2 = Trainer()
person2.login()
person2.logout()
