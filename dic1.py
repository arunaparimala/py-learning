student={
    "name":"perinba",
    "age":21,
    "major":"computer science"

}
print(student)

name,age="perinba",22
print(name,age)

print("name is",student["name"])
print("major is",student["major"])

student["gpa"]=3.8
student["age"]=22
print(student)

del student["major"]
print("after removing",student)

is_age_in_student="age" in student
print("is age in student",is_age_in_student)

is_graduation_year_in_student="graduation year" in student
print("is graduation year in student",is_graduation_year_in_student)

student_extra={
    "graduation_year":2015,
    "ome town":"spring field"
}
print(student.update(student_extra))
print(student)

a=student.get("gpa",3.8)
print(a)

prices={
    "apple":0.5,
    "banana":0.3,
    "orange":0.7
}
print(prices)
print(list(prices.keys()))
print(list(prices.values()))

print(prices.items())

for val in prices.items():
    print("fruit price is:",val)

print(len(prices))

squares={}
for num in range(1,6):
    squares[num]=num*num
print(squares)

print(prices.items())

for product,product_value in prices.items():
    print("product",product,"is",product_value)


print(prices.clear())  
print(student.copy())
student["name"]="carlie"
print(student)

keys=["name","age","major"]
values=["eve",20,"matematics"]
for val in zip(keys):
    print(val)

print(student.items())

for val in student.items():
    print(val)

fruits=["apple","banana","banana","orange","apple","banana"]
fruit_count={}
for fruit in fruits:
    fruit_count[fruit]=fruit_count.get(fruit,0)+1
    print(fruit_count)


print(student.get("gpa"))
print(student.get("graduation year",2025))
scool={
    "student1":{
        "name":"alice",
        "age":"21"
    },
    "student2":{
        "name":"bob",
        "age":22
    }
}
print(scool["student2"]["age"])
scool.setdefault("advisor","dr.smit")
print(scool)
scool.setdefault("advisor","aruna")

keys=["name","age","major"]
values=["eve","30","science"]
sample_dic=dict(zip(keys,values))
print("dictionary",sample_dic)

for key,value in student.items():
    print(key,value)
    
fruits=["apple","banana","banana","orange","apple","banana"]
fruit_count={}
for fruit in fruits:
    fruit_count[fruit]=fruit_count.get(fruit,0)+1
print(fruit_count)

from collections import defaultdict
fruit_count_coll=defaultdict(int)
for fruit in fruits:
    fruit_count_coll[fruit]=fruit_count_coll.get(fruit,0)+1
print(fruit_count_coll)
