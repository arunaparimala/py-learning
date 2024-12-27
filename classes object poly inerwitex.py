#create a base class "sape" and create a metod in "area" its return 0.create a derived class "rectangle" tat inerits from sape and overrides area metod
#to calculate and return te area of te rectangle

class sape():
    def area(self):
        return 0
    
class rectangle(sape):
    def area(self):
        l=80
        b=10
        print(l*b)
r1=rectangle()
r1.area()

#create a class called person wit constructor tat takes name as parameter.create aderived called student
#tat inerits from person and as a constructor tat takes parametre called grade.write a metod in student to display te name
#and grade use super keyword to acieve tis.

class person():
    def __init__(self,name):
        self.name=name
        

class student(person):
    def __init__(self,name,grade):
        self.grade=grade
        super().__init__("perinba")
    def display(self):
        print(self.name,self.grade)
        

s1=student("perinba","A")
s1.display()

#create a base class called"veicles" wit ametod start()
 #tat prints "veicle started" .create a derived class car( tat inerits from veicles and overrides start metod ()
 #tat print car started
class veicle():
    def start(self):
        print("veicle started")

class car(veicle):
    def start(self):
        print("car started")

c1=car()
c1.start()

#create base class called employee wit properties name and salary.create a derived class manager tat
#inerits from employee and adds property department.write a metod in manager to display name,salary,department

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,department):
        self.department=department
    def display(self):
        super().__init__("raji",50000)
        print(self.name,self.salary,self.department)
    
m1=manager("pysics")
m1.display()
