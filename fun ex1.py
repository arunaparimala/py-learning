def add(a,b):
    return a+b
print(add(2,3))

def painter(msg):
    print("te message is",msg)

painter("paint my ouse")

def evenorodd(num):
    if (num%2==0):
        print("even")
    else:
        print("odd")
        
evenorodd(10)

def printrange():
    for i in range(1,9):
        print(i)
printrange()

def passorfail(a):
    if(a>=35):
        print("pass")
    else:
        print("fail")
a=int(input("enter num "))
print(a)
passorfail(a) 

