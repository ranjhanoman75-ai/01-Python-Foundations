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
for key in student:     #loop throught to print keys 
    print(key)

for value in student.values():    #loop through to print values 
    print(value)
for key ,value in student.items():
    print(key,value)

student2 = student.copy()
print(student2)

print("==========Nested Dictionary==========")
student = {
    "student1":{
        "name": "noman",
        "age": 22
    },
    "student2":{
        "name": "ali",
        "age ": 23
    }
}
print(student["student2"]["name"])