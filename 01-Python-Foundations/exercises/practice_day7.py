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
            