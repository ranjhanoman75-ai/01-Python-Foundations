print("=======Program 1 =========")

name = ["Ali","Bilal","Noman"]
for item in name:
    print(item)

print("=======Program 2 =========")
items = [1,2,3,4,5]
print(items[0])
print(items[4])

print("=======Program 3 =========")
names = ["Ali","Bilal","Noman"]
names[1] = "Mukurram"
print(names)

print("=======Program 4 =========")
names = ["Noman","Ali"]
names.append("Mukurram")
print(names)

print("=======Program 5 =========")
data = ["noman",22,"Lahore"]
data.insert(0,115)
print(data)

print("=======Program 6 =========")
data = ["Saleem",67,"Lahore"]
data.remove("Saleem")
print(data)

print("=======Program 7 =========")
data = ["ali",22,"Pakistani"]
data.pop()         #remove last item
print(data)

print("=======Program 8 =========")
data = ["Noman",22,"Jhang"]
print(len(data))

print("=======Program 9 =========")
def reverse_list(text):
    reverse = []
    for i in text:
        reverse = [i] + reverse
    return reverse
lists = ["Noman "," Bilal "]
result = reverse_list(lists)
print(result)

print("=======Program 10 =========")
def sort(lst):
    n =  len(lst)
    
    for i in range(n):
        for j in range(i+1,n):
            if lst[i]>lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst
lists = [1,24,33,10,53,89]
result = sort(lists)
print(result)


lst = [2,5,21,1,10,3]
lst.sort()
print(lst)

print("=======Program 11 =========")
lists = [1,2,3,4,1,2]
result =lists.count(1)
print(lists)
print(result)


print("=======Program 12 =========")
def search (item,fnd):
    index = 0
    for i in item:
        if i == fnd:
            return f"Item is found",{index}
        index += 1
    
    return f"Not found"
items = [2,5,53,532,535]
found = int(input("Enter item to found: "))
result = search(items,found)
print(result)

print("=======Program 13 =========")
def largest_no(lst):
    largest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
            
    return largest
        
item = [2,42,524,52]
result = largest_no(item)
print(result)

print("=======Program 14 =========")
def smallest_no(lst):
    smallest = lst[0]
    for i in lst:
        if i <smallest:
            smallest = i
        
    return smallest
item = [2,5,634,633,1]
result = smallest_no(item)
print(result)

print("=======Program 15 =========")         
def add(lst):
    sum = 0
    for i in lst:
        sum = sum+i

    return sum
    
item = [2,4,2,52,53]
result = add(item)
print(result)
print("=======Program 16 =========")
lists = [2,33,22,52]
lists1 = []
lists1=lists.copy()
print(lists1)

print("=======Program 17 =========")
lists= [2,13,45,35,63]
list1= [13,424,52,52]
list2= []
list2 = lists+ list1
print(list2)
print("=======Program 18 =========")
def even(lst):
    even = 0 
    odd = 0
    for i in Lists:
        if i % 2==0:
            even+=1
        elif i%2!=0:
            odd+=1
    print("Even number counts are: ",even)
    print("Odd numbers count are: ",odd)

Lists = [2,52,52,5,7,9]
result = even(Lists)
