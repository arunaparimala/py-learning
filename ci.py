def compound_interest():
    if n>=2:
      return (p*((100+r)/100)*((100+r)/100))
    elif n>=3:
       return (p*((100+r)/100)*((100+r)/100)*((100+r)/100))
    else:
       print("invalid data")
p=int(input("enter principle"))
n=int(input("enter year"))
r=int(input("enter rateofinterest"))
print(compound_interest()+p)
print(round(compound_interest(),2))