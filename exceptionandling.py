print("good")
print("bye")
#printn("b")      #name error-compile time error

#logical error
a=2
b=3
print(a+a) 
#runtime error
try:
    a=input("enter a")
    b=input("enter b")
    print(a+b)
except Exception as e:
    print("someting",e)

#ex
try:
    a=int(input())
    b=int(input())
    c=int(input())
    print(b/c)
except ValueError as e:
    print("valueerror",e)
except TypeError as e:
    print("typeerror",e)
except Exception:
    print("someting wrong")
finally:
    print("done")