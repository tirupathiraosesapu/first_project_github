# Lambda Functions

def add(a, b):
    return a+b

value1 = add(1, 2)
# print(value1)
# print(add(10, 30))

value = lambda a, b: a+b
# print(value(1, 2))
# print(value(10, 30))

def evenOrOdd(a):
    if a%2==0:
        return "Even"
    else:
        return "Odd"
    
# print(evenOrOdd(8))
# print(evenOrOdd(7))

checking = lambda a : "Even" if a % 2==0 else "Odd"

# print(checking(8))
# print(checking(7))

surya = checking(25)
# print(surya)
# print(surya)
# print(surya)


# -----------------------------------------
# List Comprehensions

new_list = []

for i in range(1, 11):
    new_list.append(i)
print(new_list)

list_comp = [i for i in range(1, 11)]
print(list_comp)


even_list = []

for x in range(1, 21):
    if x%2==0:
        even_list.append(x)
print(even_list)

even_numbers = [x for x in range(1, 21) if x%2==0]
print(even_numbers)

evens = [x for x in list_comp if x%2==0]
print(evens)

odds = [x for x in even_list if x%2!=0]
print(odds)

numbers = list(filter(lambda x : x%2==0, new_list))
print("Numbers", numbers)

# -------------------------
matrix = [[1, 2], [3, 4]]

for x in matrix:
    # print(x)
    for y in x:
        print(y)

new_matrix = [y for x in matrix for y in x]

print(new_matrix)

table = [x*y for x in range(1, 4) for y in range(1, 4)]
print(table)
print("-------------------------------")
# ---------------------------------
# Lambda inside sorting

nums = [45, 30, 23, 67, 55, 10]

print(sorted(nums))
print(sorted(nums, key=lambda x : x%10))

dictionary = {"a":5,"b":3, "c":7 }

print(sorted(dictionary.items(), key=lambda x:x[1]))