print("========== Student Management System ==========")

import logging
import logging_config

students = []


def add_student():
    try:
        name = input("Enter Student Name: ").strip()
        rollno = int(input("Enter Roll Number: "))
        course = input("Enter Course: ").strip()

        # Duplicate Roll Number Check
        for student in students:
            if student["rollno"] == rollno:
                print("Roll Number already exists.")
                logging.warning(f"Duplicate Roll Number Attempt: {rollno}")
                return

        student = {
            "name": name,
            "rollno": rollno,
            "course": course
        }

        students.append(student)

        print("Student Added Successfully.")
        logging.info(f"Student Added -> Name:{name}, Roll:{rollno}, Course:{course}")

    except ValueError:
        print("Roll Number must be numeric.")
        logging.error("Invalid Roll Number entered while adding student.")


def display_students():
    if not students:
        print("No Students Found.")
        logging.warning("Display requested but student list is empty.")
        return

    print("\n========== Student List ==========")

    for student in students:
        print(f"Name   : {student['name']}")
        print(f"RollNo : {student['rollno']}")
        print(f"Course : {student['course']}")
        print("-" * 30)

    logging.info("Displayed all students.")


def search_student():
    name = input("Enter Student Name to Search: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found")
            print(f"Name   : {student['name']}")
            print(f"RollNo : {student['rollno']}")
            print(f"Course : {student['course']}")

            logging.info(f"Student Found -> {name}")
            return

    print("Student Not Found.")
    logging.warning(f"Search Failed -> {name}")


def update_student():
    try:
        rollno = int(input("Enter Roll Number to Update: "))

        for student in students:
            if student["rollno"] == rollno:

                print("\nCurrent Details")
                print(student)

                student["name"] = input("Enter New Name: ").strip()
                student["course"] = input("Enter New Course: ").strip()

                print("Student Updated Successfully.")

                logging.info(f"Student Updated -> Roll:{rollno}")

                return

        print("Student Not Found.")
        logging.warning(f"Update Failed -> Roll:{rollno}")

    except ValueError:
        print("Invalid Roll Number.")
        logging.error("Invalid Roll Number entered while updating.")


def delete_student():
    name = input("Enter Student Name to Delete: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)

            print("Student Deleted Successfully.")

            logging.info(f"Student Deleted -> {name}")

            return

    print("Student Not Found.")
    logging.warning(f"Delete Failed -> {name}")


def exit_program():
    logging.info("Student Management System Closed.")
    print("Thank you for using Student Management System.")


while True:

    print("\n========== MENU ==========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    try:
        choice = int(input("Enter Choice (1-6): "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            exit_program()
            break

        else:
            print("Invalid Choice.")
            logging.warning("Invalid Menu Choice Selected.")

    except ValueError:
        print("Please Enter Numbers Only.")
        logging.error("User entered invalid menu choice.")