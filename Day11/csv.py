import csv

"""student_details = open("student-details.csv", "r")

data = csv.reader(student_details)

mobile_numbers = []

count = 0

for row in data:
    print(row)
    count+=1
    mobile_numbers.append(row[2])

print(mobile_numbers)
print(count)

student_details.close()"""


# -------------------------------

"""question_list = []

with open("../html-2.csv", 'r') as charan:
    data = csv.reader(charan)

    for row in data:
        # print(row)
        question_list.append(row[11])

question_list.remove("Question")

print(question_list)"""

# -------------------------------

"""with open("./course/course-details.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Id", "Name", "Course", "Batch"])
    writer.writerow(["1234", "Surya", "Python Full Stack", "April 2026"])"""


"""course_details = [
    ["Id", "Name", "Course", "Batch"], 
    ["1234", "Surya", "Python Full Stack", "April 2026"]
]

with open("./course/course.csv", 'w', newline="") as file:
    writer = csv.writer(file)

    writer.writerows(course_details)"""

# --------------------------------

# Append Mode


name = input("Enter your name : ")
age = input("Enter your age : ")


with open("./students/students.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([name, age])