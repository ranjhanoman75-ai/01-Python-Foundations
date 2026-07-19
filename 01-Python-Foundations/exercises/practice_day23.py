print("===========Day 23============")
print("============Decorators===========")
def greet():
    print("Hello Noman")


def login():
    print("Login successfull")

def logout():
    print("Logout successfull")

def run(func):
    print("Program started")

    func()

    print("Program ended")

run(greet)
run(login)
run(logout)
def decorator(func):
    def wrapper():
        print("start")

        func()

        print("end")
    return wrapper
@decorator
def welcome():
    print("Hello Noman")

welcome()
print("========Login Decorator=========")
def decorator(func):
    def act():
        print("Checking user....")

        func()

        print("Access granted")
    return act
@decorator
def login():
    print("Login Successfull")
login()
print("===========Execution Logger===========")
def decorator(func):
    def wrap():
        print("Function started....")

        func()

        print("Function finished")
    return wrap
@decorator
def calculate_salary():
    print("salary calculated")
calculate_salary()
@decorator
def calculat_fee():
    print("Fee calculated")
calculat_fee()
@decorator
def calculate_marks():
    print("marks calculated")
calculate_marks()

print("==========Authentication Decorator============")
def decorator(func):
    log_in = True
    def wrapper():
        if log_in == True:
            print("Access granted")
        else:
            print("Access denied")
        func()
    return wrapper
@decorator
def login():
    print("login successfull")
login()
        