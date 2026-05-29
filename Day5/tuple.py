# Tuples in Python
# Once created never edited

first_tuple = (1, 2, 3, 4, 5)
# print(first_tuple)

duplicate_values = ("Manisha", "Kiran", "Surya", "Rehman", "Surya")

# print(duplicate_values)
# print(duplicate_values[3])

for x in duplicate_values:
    # print(x)
    pass

different_elements = tuple((10, 20, 20, 50, 40, 30))
# print(different_elements, type(different_elements), len(different_elements))

# single = (3,)
single = ("rehman",)
# print(single, type(single))

# a, b, c, d, e, f = different_elements
a, b, c, *d = different_elements

print(a)
print(b)
print(c)
print(d)

a = "Welcome", "HTML", "Python", "Java", "Java"
print(a, type(a))

print(a.count("Java"))
print(a.index("Java"))