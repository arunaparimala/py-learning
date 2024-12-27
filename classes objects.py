class goa:
    drink=""
    name=""
    def party(self):
        print("lets party...")
    def beac(self):
        print("enjoying beac")
kavi=goa()
pavi=goa()

kavi.party()
pavi.beac()

kavi.name="kavi"
pavi.name="pavi"


kavi.drink="yes"
pavi.drink="no"
print(kavi.name)
print("drink",kavi.drink)
print(pavi.name)
print("drink",pavi.drink)

#create a class laptop and create variables price,processor,name
#object p,lenova..,dell
class laptop():
    price=0
    processor=""
    ram=""

lenova=laptop()
dell=laptop()

lenova.price=50000
lenova.processor="i7"
lenova.ram="8GB"

dell.price=60000
dell.processor="i9"
dell.ram="16gb"

print(dell.price)
print(lenova.price)


