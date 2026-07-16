print("=============Abstract classes=============")
print("========== 1 Program========")
from abc import ABC, abstractmethod
class Animal(ABC):
    def eat(self):
        print("Animal is eating")
    @abstractmethod
    def sound(self):
        pass 
class dog(Animal):
    def sound(self):
        print("Dog is barking")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
class Lion(Animal):
    def sound(self):
        print("Lion is roaring")
dg = dog()
dg.eat()
dg.sound()
cat = Cat()
cat.eat()
cat.sound()
lion = Lion()
lion.eat()
lion.sound()
print("==========2 program========")
class vehicle(ABC):
    def show_company(self):
        print("Vehicle company")
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
    def fuel(self):
        pass
class Car(vehicle):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
    def fuel(self):
        print("Fuel: petrol")
class Bike(vehicle):
    def start(self):
        print("Bike started")
    def stop(self):
        print("Bike stopped")
    def fuel(self):
        print("Fuel: petrol")
class Truck(vehicle):
    def start(self):
        print("Truck started")
    def stop(self):
        print("Truck stopped")
    def fuel(self):
        print("Fuel: petrol")
print("==========Car=======")
car = Car()
car.show_company()
car.start()
car.stop()
car.fuel()
print("============Bike=========")
bike = Bike()
bike.show_company()
bike.start()
bike.stop()
bike.fuel()
print("========Truck===========")
truck = Truck()
truck.show_company()
truck.start()
truck.stop()
truck.fuel()
print("========3 program===========")
class Notification(ABC):
    def notification_info(self):
        print("sending notification...")
    @abstractmethod
    def send(self):
        pass
    @abstractmethod
    def receive(self):
        pass 
class Email(Notification):
    def notification_info(self):
        print("sending email  notification.....")
    def send(self):
        print("Sending emial  " )
    def receive(self):
        print("Email received")
class SMS(Notification):
    def notification_info(self):
        print("SMS notification.....")
    def send(self):
        print("Sending SMS")
    def receive(self):
        print("Sms received ")
class Whatsapp(Notification):
    def notification_info(self):
        print("Whatsapp notification.....")
    def send(self):
        print("Sending whatsapp message....")
    def receive(self):
        print("Whatsapp received. ")
print("========Email class======")
email = Email()
email.notification_info()
email.send()
email.receive()
print("=======SMS class========")
sms = SMS()
sms.notification_info()
sms.send()
sms.receive()
print("========Whatsapp Class=======")
whatsapp = Whatsapp()
whatsapp.notification_info()
whatsapp.send()
whatsapp.receive()

print("========4 program=========")
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Recatangle(Shape):
    def area(self,length,width):
        return length*width
    def perimeter(self,length,width):
        return 2*length*width
class Circle(Shape):
    def area(self,r):
        return 3.14 *r*r
    def perimeter(self,r):
        return 3.14*r
class Triangle(Shape):
    def area(self,base,heigth):
        return (1/2*base*heigth)
    def perimeter(self,left,right,bottom):
        total = left+right+bottom
        print("The perimeter of Triangle: ",total)
print("=======Rectagle Area=======")
rectangle = Recatangle()
print("The area of Rectangle: ",rectangle.area(4,5))
print("The perimter of rectangle: ",rectangle.perimeter(4,5))
print("======Circle Area=========")
circle = Circle()
print("The area of circle: ",circle.area(4))
print("The perimeter of circle: ",circle.perimeter(4))
print("=========Triangle Area==============")
triangle = Triangle()
print("Area of Triangle: ", triangle.area(4,6))
triangle.perimeter(4,6,7)
