#  File handling in Python


# Reading a file
"""reading_file = open("welcome.txt", "r")

print(reading_file.read())
print()
# print(reading_file.readline())
print()
# print(reading_file.readlines())

reading_file.close()"""

# Writing a file

"""writing_file = open("students.txt", "w")
# name = input("Enter your name :")
# age = input("Enter your age")
# writing_file.write(f"Student name is {name}\nStudent Age is {age}\n")
writing_file.write("This data is adds from the python program")
# writing_file.write("This data the checking purpose")

writing_file.close()"""

username = input("Enter your name")
another_file = open(f"./student/{username}.txt", "w")

another_file.write(f"This is {username}")
another_file.close()


# append file

"""append_file = open("students.txt", "a")

append_file.write("\nThis si added from the append mode")

append_file.close()"""


# read with keyword

"""
with open("students.txt", "r") as file:
    print(file.read())"""


# program
"""name = input("Enter your name : ")
age = input("Enter your age : ")
mobile_number = input("Enter your number")
course = input("Enter your course")


with open("./students/student-details.txt", "a") as file:
    file.write(f"Name: {name}\nAge: {age}\nMobile Number: {mobile_number}\nCourse: {course}\n--------------------------------\n")

print("User saved succesffully")"""