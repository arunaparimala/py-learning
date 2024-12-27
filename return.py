s_username="perinba"
s_password="123"

uname=input("enter uname")
password=input("enter password")

def verification():
    if(s_username==uname and s_password==password):
       return True
    else:
       return False
a=verification()
print(a)



def add(n1,n2):
   return n1+n2

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

added=add(a,b)
output=added*c

print(output)