delivery=["box","books","scale","pen"]
print(delivery)
delivery.append("sketc")
print(delivery)

print(delivery[0])
delivery.insert(3,"pencil")
print(delivery)

delivery.remove("box")
print(delivery)

delivery.pop()
print(delivery)

delivery.insert(2,"scale")
print(delivery)

print(delivery.index("pencil"))
print(delivery[0:3])
print(delivery)
delivery.sort()
print(delivery)
delivery.reverse()
print(delivery)
dir(delivery)
a=[1,2,3,4,5,6]
a.append(8)
print(a)
a.pop(2)
print(a)
a.insert(3,"perinba")
print(a)
a.remove(4)
print(a)
a.reverse()
print(a)
b=[10,20,30,40,50]
a.extend(b)
print(a)

print(delivery[0:3])

#add elements from oter iterable
delivery_add=["laptop","tablet","pone"]
delivery.extend(delivery_add)
print(delivery)

#wile loop in list
i=0
while i<len(delivery):
    print(delivery)
    i=i+1

#for loop in list
for i in delivery:
    print(i)

l=[]
print("type is",type(l))

l1=[1,2,3,4,5]
l2=[5,6,7,8]
print(l1+l2)

a=[2,3,4,5,-2,-7,-9]
positive=0
negative=0
for i in a:
   if i> 0:
    positive=positive+1
    print("positive number",positive)
   else:
    negative=negative+1
    print("negative number",negative)