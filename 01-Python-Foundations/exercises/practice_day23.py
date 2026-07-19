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
    log_in = False
    def wrapper():
        if log_in :
            print("Access granted")
            func()
        else:
            print("Access denied")
        
    return wrapper
@decorator
def login():
    print("login successfull")
login()
print("================Bank Transaction decorator==========")
def decorator(func):
    def wrapper():
        print("=========Transaction Started===========")   

        func()

        print("==========Transaction Ended============")
    return wrapper
@decorator
def deposit():
    print("Amount deposited")
deposit()
def withdraw():
    print("Amount Withdrawn")
withdraw()
@decorator
def check_balance():
    print("Balance checked")
check_balance()