
grocerryinventry={
    "turmeric":10,
    "salt":50,
    "goldwinner":50,
    "mustard":5,
    "cumin":6,
    "rice":600,
}
print(grocerryinventry)

for val in grocerryinventry.items():
    print(val)

#user interface
print("welcome to grocerryinvetry")
print("select items from menu")
item1=input()
item2=input()
item3=input()

#operationcoice
print("1.add")
print("2.view")
print("3.update")
print("4.delete")

coice=int(input("enter coice"))
if coice==1:
    additems=input()
    print(item1,item2,additems)
elif coice==2:
    print("view list",grocerryinventry)
elif coice==3:
    grocerryinventry["salt"]=grocerryinventry["salt"]-5
    grocerryinventry["cumin"]=grocerryinventry["cumin"]-5
    print("updated list",grocerryinventry)
elif coice==4:
    del grocerryinventry["salt"]
    print(grocerryinventry)
else:
    print("tq for purcasing our grocerryinventry")
