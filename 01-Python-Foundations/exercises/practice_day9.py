student = {
    "name": "Noman",
    "Age" : 22,
    "city": "Jhang"
    }
print(student)
print(student["name"])
print(student["Age"])
student["course"]= "BSSE"
print(student)
student["course"]= "Software Engineering"
print(student)
student.pop("Age")
print(student)
del student["course"]
print(student)
print(len(student))
if "age" in student:
    print("found")
else:
    print("Not found")

print(student.keys())
print(student.values())
print(student.items())
for key in student:
    print(key)

for value in student.values():
    print(value)