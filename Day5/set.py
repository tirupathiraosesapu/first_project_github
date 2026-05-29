# Sets in Python

students = {1, 4, 7, 9, 5, 3, 3, 2, 4, 1}
print(students)

different_data = {20, 40.5, True, False, "WElcome", 20}
# print(different_data[1])
different_data.add("Python")
different_data.add(True)
different_data.add(30)
print(different_data)

different_data.remove(30)
print(different_data)

different_data.discard("Python")
print(different_data)

different_data.pop()
different_data.pop()
different_data.pop()
# different_data.clear()
print(different_data)

value = frozenset(different_data)

value.add("eror")