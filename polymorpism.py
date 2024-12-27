def add(a,b,c=0):
    print(a+b+c)
add(10,20)
add(10,10)

#ex in polymorpism
class animal():
    def sound(self):
        print("animal names sound")

class dog(animal):
    def sound(self):
        print("dog barks")

class bird(animal):
    def sound(self):
        print("birds sings")

b1=bird()
b1.sound()