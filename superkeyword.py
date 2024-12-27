class a():
    def __init__(self):
        print("A")
    def display(self):
        print("you are in class A")

class b():
    def __init__(self):
        super().__init__()
        print("B")
        
    def display(self):
        print("you are in class B")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")
    def display(Self):
        print("you are in c class")


obj1=c()
