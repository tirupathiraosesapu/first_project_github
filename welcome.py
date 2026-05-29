from collections import Counter, defaultdict

numbers = [1, 2, 3, 1, 4, 5, 2, 4, 1, 3, 3, 3]
# numbers = "Python Full Stack"
# numbers = ["HTML", "CSS", "JavaScript", "React"]

result = Counter(numbers)
# print(result.most_common(3))
data = {}
print(data, type(data))
data = defaultdict(dict)
print(data, type(data))

data["name"].append("Python")
print(data["name"], type(data))
