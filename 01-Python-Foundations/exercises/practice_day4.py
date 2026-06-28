for i in range(5):
    print("Hello Noman")

for i in range(1,101,2):
    print(i)


count = 10
while count>0:
    print(count)
    count-=1

count = 1
while count<11:
    print(count)
    count+=1

num = int(input("Enter a number: "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)


sum = 0
for i in range(1,101):
    sum+=i
    print(f"The sum of first 100 numbers is: {sum}")


num = int(input("Enter a number:"))
for i in range(1,101):
    if i%5==0:
        print("The numbers that are divisible by 5",i)
    else: 
        print("The numbers that are not divisible by 5 ",i)
