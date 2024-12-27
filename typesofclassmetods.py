class pone():
    carger_type="c_type"
    def __init__(self):
        self.brand=""
        self.price=34
    def set_price(self,price):
        self.price=price

    def get_price(self):
        print(self.price)

    @classmethod #decorator
    def cange_carger_type(cls):
        cls.carger_type="B type"
        print("carger type is canged to B")
    @staticmethod #decorator
    def info():
        print("tis is pone class")
nokia=pone()
nokia.set_price(10000)
nokia.get_price()

pone.cange_carger_type()
nokia.info()