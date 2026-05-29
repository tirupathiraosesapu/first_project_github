def welcome():
    return 1
    return 2


items = welcome()
# print(items, type(items))


def anotherFunction():
    # yield 1
    # yield 2
    # yield 3
    for i in range(1, 10):
        yield i


item = anotherFunction()
# print(item, type(item))

# print(item.__next__())
# print(item.__next__())
# print(item.__next__())
# print(item.__next__())

# print(next(item))

# for i in item:
#     print(i)


generator1 = (i for i in range(6))
# print(generator1, type(generator1))

# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))


def student_generator():

    for i in range(1, 1000001):

        student = {
            "id": i,
            "name": f"Student_{i}",
            "course": "Python Full Stack",
            "progress": f"{i % 100}%",
        }

        yield student


students = student_generator()

# print(next(students))
# print(next(students))

for _ in range(10):
    print(next(students))
print("----------------------")
for _ in range(10):
    print(next(students))
