print("This is the step 1")

"""
try:
    statement
except:
    error message
"""
"""num = int(input("Enter a numerator value : "))
value = int(input("Enter a denominator Value : "))
try:
    print(num/value)
except ZeroDivisionError:
    print("It is a zero division error")
finally:
    print("Exception handling is comleted")"""

list_values = [1, 2, 3, 4, 5]
try:
    print(list_values[8])
except IndexError:
    print("List index is out of range")

try:
    file = open("welcome.txt", "r")
    print(file)
except FileNotFoundError:
    print("File is not founded")



try:
    num = int(input("Enter your number"))
    print(100/num)
except ValueError as e:
    print("Values error", e)
except ZeroDivisionError as error:
    print("It is a zero division error", error)


try:
    num = int("Abc")
except Exception as e:
    print("Last error in this file",e)

try:
    print(10+"7")
except Exception as e:
    print("Type error : ", e)

print("This si the final step")