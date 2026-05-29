
first_name = "Tirupathi Rao"

employees = ["Tirupathi", "Rehman", "Surya"]

student_data = [1, "Surya", "B.Tech", "Hyderabad", 1234567890]

# students = { key1:value1, key2:value2}
students = {"id":1, "full_name":"Harshik", "qualification":"B.Tech", "number":1234567890}
print(students)

# print(students["Full name"])
# print(students["Qualification"])
# print(students["Id"])
# print(students.get("id"))
# print(students.get("number"))
# print(students["number"])

students["Full name"] = "Manisha"
print(students)

students["Address"] = "Hyderabad"
print(students)

print(students.keys())
print(students.values())
print(students.items())

print("-------------------------------------")
# for keys in students:
for keys in students.keys():
    print(keys, students[keys])

print("-------------------------------------")

for values in students.values():
    print(values)

print("-------------------------------------")

for key,values in students.items():
    print(f" Key:{key}, value:{values}")

print("-------------------------------------")

students.update({"Address":"Vijayawada"})
print(students)

students.pop("Full name")
print(students)

print("-------------------------------------")

students_details = {
    1:{"name":"Surya", "age":25},
    2:{"name":"Kiran", "age":29}
}

# print(students_details[1]["name"])

for key, values in students_details.items():
    print("--------")
    print("Student Id:", key)
    for key1, value1 in values.items():
        print(f"Student {key1} :", value1)

