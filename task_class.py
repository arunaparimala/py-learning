class cocolate():
    def __init__(self,name,flavour):
        self.name=name
        self.flavour=flavour
    def display(self):
        print("cocolate name is",self.name)
        print("flavour is",self.flavour)

ecolairs=cocolate("name","flavour")
ecolairs.name="ecolairs"
ecolairs.flavour="strawberry"

ecolairs.display()

#create a class in flower
class flower():
    name=""
    colour=""
flower1=flower()
flower2=flower()

flower1.name="rose"
flower1.colour="red"

flower2.name="lotus"
flower2.colour="pink"
print(f"Name:{flower1.name},Colour:{flower1.colour}")
print(f"Name:{flower2.name},colour:{flower2.colour}")

#class metods-a function is defines inside a class
class garden():
    lengt=""
    breadt=""
    def area_garden(self):
        print("area is",self.lengt*self.breadt)
square=garden()

square.lengt=10
square.breadt=10
square.area_garden()

#
class employee():
    def __init__(self,name,id,dep):
        self.name=""
        self.id=""
        self.dep=""
employee1=employee("name","id","dep")
employee2=employee("name","id","dep")

employee1.name="raju"
employee1.id=51331
employee1.dep="devoloper"

employee2.name="ram"
employee2.id=51332
employee2.dep="tester"

print(f"Name:{employee1.name},id:{employee1.id},dep:{employee1.dep}")
print(f"Name:{employee2.name},id:{employee2.id},dep:{employee2.dep}")

#__str__function
class person():
    def __init__(self,name,place):
        self.name=name
        self.place=place
    def __str__(self):
        return f"{self.name},{self.place}"
person1=person("perinba","chennai")
print(person1)







