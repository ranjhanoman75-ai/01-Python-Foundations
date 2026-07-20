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