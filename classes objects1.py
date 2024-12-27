class pc:
    def __init__(self):#init -constructor(in built functions)
        self.ram=""
        self.processor=""
    def display(self):
        print("ram:",self.ram)
        print("processor",self.processor) #self-denotes current object
dell=pc()
lenova=pc()

dell.processor="6Gb"
dell.ram="i5"

lenova.processor="16GB"
lenova.processor="i8"

dell.display()
lenova.display()


#examples
class student():
    def __init__(self):
        self.name="abcde"
        self.regnum="12345"
    def display(self):
        print("name:",self.name)
        print("reg num",self.regnum)
s1=student()
s2=student()

s1.name="aruna"
s1.regnum=1

s2.name="aswini"
s2.regnum=2

print(s1.name)
print(s1.regnum)
s1.display()
s2.display()



#example 3
#create class fruit,variable color init__ Metod create a object
 #called apple "pass te color variable as parameter" 

class fruit():
    def __init__(self,col):
        self.color=col
apple=fruit("red")
print(apple.color)

#example 4
class teacer():
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("name:",self.name)
        print("regno:",self.regno)

t1=teacer("parimala",1)
t2=teacer("maa",2)

t1.display()
t2.display()

#example 4
class calculator():
    def __init__(self,a,b):
        self.num1=10
        self.num2=10
    def add(self):
        return ("add",10+10)
    def sub(self):
        return (10-10)
    def mul(self):
        return (10*10)
    def div(self):
        return (10/10)
obj1=calculator(10,10)
print(obj1.add())
print(obj1.sub())
print(obj1.mul())
print(obj1.div())


#different types of variables
class smpone():
    cargertype="ctype"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("brandnd:",self.brand)
        print("price",self.price)
        print("cargertype",self.cargertype)
oppo=smpone("oppo","10000")
samsung=smpone("samsung","15000")
realme=smpone("realme","20000")


samsung.display()

oppo.display()

realme.display()