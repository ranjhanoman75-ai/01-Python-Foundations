print("========Student Management System=======")
print("===========Menu=============")
Students = []
def add_student():
    name = input("Enter the name of the student: ")
    rollno = int(input("Enter the roll no of the student: "))
    course = input("Enter the course of the student: ")

    student = [name,rollno,course]
    Students.append(student)
    print("Student added successfully! ")

def display_student():
    if len(Students) == 0:
        print("No student found ")
        return
    else:
        for student in Students:
            print("Name: ", student[0])
            print("Roll No: ", student[1])
            print("Course: ", student[2])
            print("-"* 30)



def search_student():
    name = input("Enter the name of student to find: ")
    found = False
    if len(Students) == 0:
        print("List is empty! ")
        return
    for student in Students:
        if student[0].lower()==name.lower():
            print("Student found ")
            print("Name: ", student[0])
            print("Roll No: ", student[1])
            print("Course: ", student[2])
            print("-"* 30)
            found = True
            break
    
    if not found:
        print(" Student not found ")
    

def update_student():  
    if len(Students)== 0:
        print("List is empty ")
        return 
    found = False
    rollno = int(input("Enter the roll no of the student: "))
    for student in Students:
        if student[1]  == rollno:
            print ("Current details: ")  
            print("Name: ", student[0])
            print("Roll No: ", student[1])
            print("Course: ", student[2])
            print("-"* 30)

            print("\n Enter the new details: ")  
            student[0] = input("Enter the new name: ")
            student[1] = int(input("Enter the new roll no: "))
            student[2]= input("Enter the new course: ")

            print("Student updated successfully ")
            found = True
            break
    if not found:
        print("Student not found")
    

def delete_student():
    found = False
    name = input("Enter the name of the student you want to delete: ")
    if len(Students)==0:
        print("List is empty ")
        return
    for student in Students:
        if student[0].lower()== name.lower():
            Students.remove(student)
            print("Student deleted successfully! ")
            found = True
            break
    if not found:
        print("Student not found")

def exit_program():
    print ("Thank you for using this system ")

while True:
    print("1: Add Student ")
    print("2: Display Student ")
    print("3: Search Student ")
    print("4: Delete Student ")
    print("5: Update Student ")
    print("6: Exit Program ")

    choice =  int(input("Enter your choice:(1-6) "))

    if choice==1:
        add_student()
    elif choice ==2:
        display_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        update_student()
    elif choice == 6:
        exit_program()
        break
    else: 
        print("Invalid Choice")