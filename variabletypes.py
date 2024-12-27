class pone():
    def __init__(self,brand,price,cargertype):
        self.brand=brand
        self.price=price
        self.cargertype=cargertype
    def display(self):
        print("brand",self.brand)
        print("price",self.price)
        print("cargertype",self.cargertype)
samsung=pone("samsung",15000,"ctype")
samsung.display()

oneplus=pone("oneplus",30000,"btype")
oneplus.display()