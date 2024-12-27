#multilevel ineritance
class grandpa():
    def car(self):
        print("grandpa's car")
    
class dad(grandpa):
    def money(self):
        print("dad's money")

class daugter(dad):
    def jewels(self):
        print("daugters jewels")

perinba=daugter()
perinba.jewels()
perinba.car()
perinba.money()

dana=dad()
dana.money()
dana.car()

#hierarical ineritance & ybrid ineritance
class dad():
    def money(self):
        print("dad's money")

class land():
    def important(self):
        print("important land")

class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

ram=son1()
ram.money()
ram.important()

#single inheritance
class grandpa():
    def house(self):
        print("grandpa's house")

class dad(grandpa):
    def bike(self):
        print("dads bike")
dhana=dad()
dhana.bike()
dhana.house()

#multiple inheritance
class grandma():
    def bangles(self):
        print("grandma's bangles")
class mother():
    def necklace(self):
        print("mother's necklace")
class daugter(grandma,mother):
    def ring(self):
        print("daughter's ring")
perinba=daugter()
perinba.ring()
perinba.necklace()
perinba.bangles()

#multilevel ineritance
class grandpa():
    def apartment(self):
        print("grandpa's apartment")
class mom(grandpa):
    def savings(self):
        print("mom's saving")
class chithi(mom):
    def money(self):
        print("citi's saving")
raji=chithi()
raji.money()
raji.savings()
raji.apartment()

    
#ierarical ineritance
class scool():
    def place(self):
        print("obey discipline")
    
class student1(scool):
    def study(self):
        print("study science")

class student2(scool):
    def study(self):
        print("study tamil")

s1=student1()
s2=student2()
s1.place()
s1.study()
s2.place()
s2.study()
    




