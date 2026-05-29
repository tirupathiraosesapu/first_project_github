from collections import Counter, defaultdict

# student_marks = [99, 99, 55, 74, 38, 99]
student_marks = ["Python Full Stack", "Python Full Stack", "MERN Stack", "DATA Science"]
student_marks = "Python Full Stack"
student_marks = (1, 3, 5, 2, 6, 1, 7)
# print(student_marks, type(student_marks))
result = Counter(student_marks)

# print(result.most_common(3), type(result))
# print(result.elements(), type(result))


# first_dictionary = {}
first_dictionary = defaultdict(set)
print(first_dictionary, type(first_dictionary))
# first_dictionary["Name"] = "value"
# first_dictionary["Name"].append("Value")
first_dictionary["age"].add(30)
# first_dictionary["age"] = 30

print(first_dictionary, type(first_dictionary))
