print("=========University Mangement System=========")
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person(self):
        print(f"Name of person : {self.name}")
        print(f"Age of person: {self.age}")
    def __str__(self):
        return f"Name = {self.name} , Age = {self.age}"
class Academic:
    def __init__(self,course,semester):
        self.course = course
        self.semester = semester
    def display_academic(self):
        print(f"Course is: {self.course}")
        print(f"Semester is: {self.semester}")
    def __str__(self):
        return f"Course = {self.course}, Semester = {self.semester}"
class student(person,Academic):
    def __init__(self, name, age,course,semester):
       person.__init__(self,name,age)
       Academic.__init__(self,course,semester)
    def calculate_fee(self):
        if self.semester<= 4:
            return 30000
        elif self.semester <= 6:
            return 40000
        else:
            return 50000
            
    def display_info(self):
        self.display_person()
        self.display_academic()
        print("Fee:" , self.calculate_fee())

p = person("Ali",23)
p.display_person()  
a = Academic("Ai engineer", 6) 
a.display_academic()
s1 = student("Noman",22,"Agentic Ai",5)
s1.display_info()  
    