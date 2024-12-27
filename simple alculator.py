print("simple calculator")
print("1.addition")
print("2.subraction")
print("3.multiplication")
print("4.division")
print("5.square")
print("6.cube")

coice=int(input("enter your coice 1/2/3/4/5/6"))
num1=int(input("enter num1"))
num2=int(input("enter num2"))
def operations():
   if coice==1:
      print(num1+num2)
   elif coice==2:
      print(num1-num2)
   elif coice==3:
      print(num1*num2)
   elif coice==4:
      print(num1/num2)
   elif coice==5:
      print(num1*num1)
   elif coice==6:
      print(num2**num2)
   else:
      print("coose a correct coice")
operations()