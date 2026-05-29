import json

"""student_details = {
    "name":"Kiran",
    "age":27,
    "course":"Python"
}"""

"""student_details = [1, 2, 3, 4, 5]

result = json.dumps(student_details)
print(result, type(result))
print(student_details, type(student_details))"""


"""data = '{"name":"Kiran Kumar", "Qualification":"B.Tech"}'

result = json.loads(data)

print(result["name"], type(result))
print(data, type(data))"""

count = 0
with open("product-details.json", "r") as product:
    data = json.load(product)

    """# print(data["total"], type(data))
    for keys, values in data.items():
        print(keys, values)

        if keys == "products":
            for i in values:
                count+=1"""
    
    with open("new-products.json", "w") as files:
        json.dump(data, files)

# print(count)
