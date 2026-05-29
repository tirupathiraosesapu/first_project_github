from abc import ABC, abstractmethod

# ==================================
# ABSTRACT BASE CLASS
# ==================================


class User(ABC):

    def __init__(self, user_id, name, email, password):

        # PUBLIC VARIABLES
        self.user_id = user_id
        self.name = name

        # PRIVATE VARIABLES (ENCAPSULATION)
        self.__email = email
        self.__password = password

    # ==================================
    # GETTER METHOD
    # ==================================

    def get_email(self):
        return self.__email

    # ==================================
    # SETTER METHOD
    # ==================================

    def set_email(self, new_email):

        self.__email = new_email

        print("Email updated successfully.")

    # ==================================
    # PASSWORD VALIDATION
    # ==================================

    def change_password(self, old_password, new_password):

        if self.__password == old_password:

            self.__password = new_password

            print("Password changed successfully.")

        else:
            print("Old password is incorrect.")

    # ==================================
    # ABSTRACT METHODS
    # ==================================

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def show_dashboard(self):
        pass

    # ==================================
    # NORMAL METHOD
    # ==================================

    def logout(self):

        print(f"{self.name} logged out successfully.\n")


# ==================================
# STUDENT CLASS
# ==================================


class Student(User):

    def __init__(self, user_id, name, email, password, course):

        super().__init__(user_id, name, email, password)

        # PRIVATE VARIABLE
        self.__course = course

    # GETTER METHOD
    def get_course(self):
        return self.__course

    # SETTER METHOD
    def set_course(self, new_course):

        self.__course = new_course

        print("Course updated successfully.")

    # METHOD OVERRIDING
    def login(self):

        print(f"Student {self.name} logged into LMS system.")

    # METHOD OVERRIDING
    def show_dashboard(self):

        print("Student Dashboard")

        print(f"Student Name : {self.name}")

        print(f"Course : {self.__course}")

    def submit_assignment(self):

        print(f"{self.name} submitted Python assignment.")


# ==================================
# TRAINER CLASS
# ==================================


class Trainer(User):

    def __init__(self, user_id, name, email, password, subject):

        super().__init__(user_id, name, email, password)

        self.__subject = subject

    # METHOD OVERRIDING
    def login(self):

        print(f"Trainer {self.name} logged into LMS system.")

    # METHOD OVERRIDING
    def show_dashboard(self):

        print("Trainer Dashboard")

        print(f"Trainer Name : {self.name}")

        print(f"Subject : {self.__subject}")

    def upload_notes(self):

        print(f"{self.name} uploaded course materials.")


# ==================================
# ADMIN CLASS
# ==================================


class Admin(User):

    def __init__(self, user_id, name, email, password):

        super().__init__(user_id, name, email, password)

    # METHOD OVERRIDING
    def login(self):

        print(f"Admin {self.name} logged into LMS system.")

    # METHOD OVERRIDING
    def show_dashboard(self):

        print("Admin Dashboard")

        print(f"Admin Name : {self.name}")

    def manage_users(self):

        print(f"{self.name} is managing LMS users.")


# ==================================
# POLYMORPHISM FUNCTION
# ==================================


def access_dashboard(user):

    user.login()

    user.show_dashboard()

    print("----------------------------")


# ==================================
# OBJECT CREATION
# ==================================

student1 = Student(101, "Ravi", "ravi@gmail.com", "ravi@123", "Python Full Stack")

trainer1 = Trainer(
    201, "Mani Kumar", "mani@gmail.com", "trainer@123", "Python Programming"
)

admin1 = Admin(301, "Suresh", "admin@gmail.com", "admin@123")


# ==================================
# POLYMORPHISM EXECUTION
# ==================================

users = [student1, trainer1, admin1]

for user in users:

    access_dashboard(user)


# ==================================
# ENCAPSULATION FEATURES
# ==================================

print("Student Email :", student1.get_email())

print("----------------------------")

student1.set_email("newravi@gmail.com")

print("Updated Email :", student1.get_email())

print("----------------------------")

student1.change_password("ravi@123", "newpassword@123")

print("----------------------------")

student1.set_course("Data Science")

print("Updated Course :", student1.get_course())

print("----------------------------")


# ==================================
# INDIVIDUAL FEATURES
# ==================================

student1.submit_assignment()

print("----------------------------")

trainer1.upload_notes()

print("----------------------------")

admin1.manage_users()

print("----------------------------")

student1.logout()

trainer1.logout()

admin1.logout()
