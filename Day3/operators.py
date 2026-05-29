# Operators in Python

"""
1. Arthematic opeartors (+, -, *, /, //, %, **)
2. Comparison operators (==, !=, >, <, <=, >=)
3. Assignment Operators (=, +=, -=, *=, /=, //=, %=, **=)
4. Logical Operators (and, or, not)
5. Bitwise Operators (&, `, ^, ~, <<, >>)
6. Membership operators (in, not in)
7. Identity Operators (is, is not)
"""

# 1. Arthematic opeartors (+, -, *, /, //, %, **)

a, b = 10, 20

"""print(f"Addition: {a+b}\nSubraction: {a-b}\nMultiplication: {a*b}")
print(f"Division: {a/b}\nFloor Division: {a//b}\nModulus: {a%b}\nExponentation: {a**3}")"""

# 2. Comparison operators (==, !=, >, <, <=, >=)
"""print(f" a == b : {a==b}")
print(f" a != b : {a!=b}")
print(f" a > b : {a>b}")
print(f" a < b : {a<b}")
print(f" a >= b : {a>=b}")
print(f" a <= b : {a<=b}")"""

# 3. Assignment Operators (=, +=, -=, *=, /=, //=, %=, **=)
x, y = 12, 18
# print(x, y)

x = x+a
# print(x)

y +=b
# print(y)
# print(f"Addition Assignemnt operator : {}")

# 4. Logical Operators (and, or, not)

"""print(f"a>x : {a>x}")
print(f"y<b : {y<b}")
print(f"a>x and y<b : {a>x and y<b}")
print(f"a>x or y<b : {a>x or y<b}")
print()
print(not a>b)"""

# 6. Membership operators (in, not in)

full_name = "TechU Innovations Labs Pvt Ltd"

print("S" in full_name)

print("z" not in full_name)

# 7. Identity Operators (is, is not)

m, n = 10, 10

print(m is n)
print(m is not n)