import re

"""username = input("Enter your username : ")

pattern = "admin"

result = re.match(pattern, username)

if result:
    print("Result is matched")
else:
    print("Unknown value")
"""

"""message = input("Enter any message")

pattern = "hack"

result = re.search(pattern, message)

if result:
    print("This is a harmful message")
else:
    print("This is a valid message")"""

'''products = """
Laptop Price = 50000
Mobile price = 25000
Tablet Price = 30000
"""
print(products)

pattern = "\d+"

# result = re.findall(pattern, products)
result = re.findall(r"\d+", products)
print(result)'''

"""text = "My email address is tirupathi@gmail.com"

result = re.sub(r"[a-zA-Z0-9._]+@[a-z]+\.com", "This is tirupathi email address", text)

print(result)"""

"""text = "S.No,Name,Email,Qualification,age"

result = re.split(",", text)

print(result)"""


number = "8234567890"

pattern = "^[6-9][0-9]{9}$"

if re.match(pattern, number):
    print("Number is perfect")
else:
    print("Please enter valid mobile number")
