# Lists in Python

# Collection of elements in a single variable

students = ["Manisha", "Sathvik", "Rehman", "Surya", "Manisha"]
# print(students)

# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[4])

students[0] = "Kiran"
# print(students)


list_type = [10, 12.6, "Techu Innovations", True, [0,[]], {}]


first_list = list((1, 2, 3, 4, 5))

# second_list = list(range(1, 100, 2))
second_list = list(range(1, 11))

# print(first_list, type(first_list), len(first_list))
# print(second_list, type(second_list), len(second_list))
# print(list_type[-3])

# print(second_list[:3])  #first three elements
# print(second_list[3:])  #skip the first three elements

# print(second_list[::2])
# print(second_list[::-1])

# ------------------------------
# List methods

students_data = ["Sathvik"]
print(students_data)

students_data.append("Akshay")
students_data.append(20)
students_data.append(25.5)
students_data.append([1, 2, 3])
students_data.append(False)
print(students_data)

students_data.insert(4, "Rehman")
students_data.insert(8, "Tirupathi")
# students_data.insert(-1, "Harshik", "welcome")
print(students_data)
# print(students_data[7])

students_data.extend([1, 2, 3])
print(students_data)

students_data.remove(False)
students_data.remove([1, 2, 3])
# students_data.remove("Techu")
print(students_data)

students_data.pop()
students_data.pop(4)
print(students_data)


numbers = [10, 5, 8, 4, 9, 3, 2, 6,5]
numbers.sort()
print(numbers)
# students_data.sort()
# print(students_data)
students.sort()
print(students)

value =[20.5, 19, 15, 27] 
value.sort()
print(value)

value.reverse()
print(value)

print(numbers + value)

print(numbers*3)

print( 10 in numbers)


nested_listst = [[1, 2], ["a", "b", "c"], [True, False]]
print(nested_listst[1])
print(nested_listst[1][2])
