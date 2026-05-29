# student_marks = [95, 76, 45, 99, 100, 50]
# student_marks = (95, 76, 45, 99, 100, 50)
# student_marks = "Python Full Stack"
# student_marks = 1234567890
student_marks = {"name": "Trirupathi", "Age": 20}
print(student_marks, type(student_marks))

mark = student_marks.__iter__()
print(mark, type(mark))

marks = iter(student_marks)
print(marks, type(marks))

for values in student_marks:
    print(values)
print("--------------------------")

print(mark.__next__())
print(mark.__next__())
print("--------------------------")

# for i in mark:
#     print(i)
print("--------------------------")

print(mark.__next__())
print(next(mark))
print(next(mark))
print(next(mark))
print("--------------------------")

for i in mark:
    print(i)
print("--------------------------")


print(student_marks.__next__())
