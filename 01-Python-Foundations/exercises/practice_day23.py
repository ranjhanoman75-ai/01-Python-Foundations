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