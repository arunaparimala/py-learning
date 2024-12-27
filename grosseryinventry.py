
grocerryinventry={
    "turmeric":10,
    "salt":50,
    "goldwinner":50,
    "mustard":5,
    "cumin":6,
    "rice":600,
}
print(grocerryinventry)


#add items
grocerryinventry["mustard"]=10
grocerryinventry["milk"]=35
grocerryinventry["egg"]=20
grocerryinventry["aneese"]=20
print("updatedgrocerryinventry",grocerryinventry)

#delete item
del grocerryinventry["cumin"]
print("after remove",grocerryinventry)

print("view te menu",grocerryinventry)

for val in grocerryinventry.items():
    print(val)

is_salt_in_grocerryinventry="salt" in grocerryinventry
print(is_salt_in_grocerryinventry)

#operationcoice
print("1.add")
print("2.view")
print("3.update")
print("4.delete")

coice=int(input("enter coice"))
if coice==1:
    additems=input()
    print(additems,grocerryinventry)
elif coice==2:
    print("view list",grocerryinventry)
elif coice==3:
    grocerryinventry["rice"]=grocerryinventry["rice"]-5
    grocerryinventry["egg"]=grocerryinventry["egg"]-5
    print("updated list",grocerryinventry)

elif coice==4:
    del grocerryinventry["egg"]
    print(grocerryinventry)
else:
    print("tq for purcasing our grocerryinventry")
