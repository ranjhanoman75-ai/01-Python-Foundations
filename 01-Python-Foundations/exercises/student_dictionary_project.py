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