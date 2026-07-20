print("===========Context Manager===============")
class Mycontext:
    def __enter__(self):
        print("Entering.......")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("leaving..........")
    
    def greet(self):
        print("hello noman")

with Mycontext() as obj:
    print("Inside Block")
    obj.greet()

print("===========Exception Handling=============")
class mycontext:
    def __enter__(self):
        print("Entering......")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("leaving..........")

        print("Exception type",exc_type)
        print("Exception value",exc)

with mycontext():
    print(10/2)
print("===========Bank Locker Analog============")
class locker:
    def __enter__(self):
        print("Locker openning....")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("Locker Closing.....")

    def withdraw(self):
        print("Amount withdrawn.....")

with locker() as lcker:
    lcker.withdraw()

print("===========Database Connection===========")
class database:
    def __enter__(self):
        print("Database connected........")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("Database closing.......")
    def execute(self):
        print("Executing Query...")
with database() as db:
    db.execute()