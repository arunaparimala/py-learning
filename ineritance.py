#multiple ineritance
class dad():
    def pone(self):
        print("Dad's pone")

class mom():
    def sweet(self):
        print("mom'sweet")
class son(dad,mom):
    def laptop(self):
        print("son's laptop")

yoges=son()
yoges.laptop()
yoges.pone()
yoges.sweet()

#multiple ineritance

class teacer():
    def onesubject(self):
        print("read science")

class principle():
    def management(self):
        print("no need to read and teac")

class student(teacer):
    def allsubject(self):
        print("read all subject")

dana=teacer()       
perinba=student()
perinba.allsubject()
perinba.onesubject()
dana.onesubject()