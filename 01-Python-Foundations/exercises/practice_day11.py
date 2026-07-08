import math
print(math.asin(1))
print(math.acos(1))
print(math.atan(1))
print(math.degrees(1))
print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.factorial(5))
print(math.ceil(2.4))


import random
print(random.randint(1,100))
names = ["noman","ali","bilal"]
print(random.choice(names))

from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

import os 
print(os.getcwd())
print(os.listdir())
print(os.path.exists("01-Python-Foundations/exercises/student_record.txt"))

print(os.rmdir("project"))
