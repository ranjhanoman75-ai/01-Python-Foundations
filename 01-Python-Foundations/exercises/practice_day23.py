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