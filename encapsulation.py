class company():
    def __init__(self):
        self._companyname="youtube"


                                                 #witout _ called public
                                                 #wit __ called privete it acces witin class
                                                 #_ called protected
    def companyname(self):
        print(self._companyname)
c1=company()
c1.companyname()
