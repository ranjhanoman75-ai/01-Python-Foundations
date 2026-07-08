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
if "Age" in student:
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
        "age": 23
    }
}
print(student["student2"]["name"])


print("============Mini project ===========")
student = {
    "name": "Noman",
    "Age ": 22,
    "Course": "BSSE",
    "RollNo": 24
}


while True:
    print("1: Display student")
    print("2: Update Course ")
    print("3: Add Email")
    print("4: Delete Course")
    print("5: Exit program")

    choice = int(input("Enter your choice: (1-5) "))
    if choice == 1:
        print("Name :", student["name"])
        print("Age :", student["Age"])
        print("Course :", student["Course"])
        print("RollNo :", student["RollNo"])
    elif choice == 2:
        course = input("Enter the new course:")
        student["Course"]= course
        print("Course updated successfully! ")
    elif choice == 3:
        email = input("Enter the email: ")
        student["Email"] = email
        print("Email added successfully! ")
    elif choice == 4:
        student.pop("Course")
        print("Course deleted successfully!")
        if course in student:
            student.pop("Course")
        else: 
            print("Course already deleted! ")
    elif choice == 5:
        print("Thank you for using this program! ")
        break 
    else:
        print("Invalid choice! Please enter choice(1-5)")