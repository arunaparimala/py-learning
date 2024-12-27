#print te multiples of 5 using forloop range() function
for i in range(1,20):
    mul=i*5
    print(mul)

#find te minimum element in te list
n=[40,30,60,80,90]
for i in n:
    if (n[0]>n[1]):
        print(n[1])
    elif (n[1]>n[2]):
        print(n[1])
    elif(n[3]>n[2]):
        print(n[2])
    elif (n[4]>n[3]):
        print(n[3])
    else:
        print("maximum value")

#using forloop to iterate troug letters
for i in "perinba":
    print(i)

    
#using forloop to iterate vegetables
veg=["onion","tomato","potato","brinjal"]
for val in veg:
    print(val)

#using forloop in iterate dictionaries
fruits={
    "apple":10,
    "strawberry":20,
    "cerry":30
}
for keys in fruits:
    print(keys,fruits[keys])

#using for loop in zip function
names=["aruna","raji","maa","perinba"]
rollno=[1,2,3,4,5,6]

for student in zip(names,rollno):
    print(student)

#count te elements in for loop
a=[10,20,30,40,50]
count=0
for i in a:
    count=count+1
print(count)

#print triangle stars
for i in range(1,5):
    print()
    for j in range(i):
        print( "*" ,end="")

#print square in numbers
n=[1,2,3,4,5]
for i in n:
   square=i**2
   print("square is",square)

#forloop in indexing
message="perinba"
for n in message[::2]:
    print(n)