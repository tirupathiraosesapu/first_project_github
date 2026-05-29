students = {}

while True:
    print("\n1. Add Students\n2. View Students\n3. Update Marks\n4. Delete Student\n5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter student Id")
        student_name = input("Enter student name")
        student_marks = input("Enter marks")
        students[student_id] = {"name":student_name, "marks":student_marks}
        print(students)
    elif choice =="2":
        for keys, values in students.items():
            print(f"Student Id:{keys}\nStudent Name:{values["name"]}\nStudent Marks:{values["marks"]}")
        print(students)
    elif choice == "3":
        new_id = input("Enter student ID :")

        if new_id in students:
            students[new_id]["marks"] = int(input("Enter new updated marks"))
            print(students)
        else:
            print("Student is not found")
    elif choice == "4":
        delete_id = input("Enter student Id:")
        students.pop(delete_id, None)
        print(students)
    elif choice == "5":
        break