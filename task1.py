a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=int(input("enter d"))
if a>b and d>a:
    print("a is bigger no",a,"b is smaller no",b)
elif a>b and b>a:
    print("b is bigger no",b,"a is smaller no",a)
elif b>a and c>d:
    print("c is bigger no,",c,"d is smaller no",d)
elif c>a and d>a:
    print("d is bigger no",d,"a is smaller no",a)
else:
    print("noting")


