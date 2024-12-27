a={
    "name":"perinba",
     "age":1,
     "place":"subanraopet"
}
print(a)
print(a.keys())
print(a.values())
a["food"]="poori"
print(a)
a["age"]=3
print(a)


ss_mart={

    "orange":20,
    "banana":50,
    "carrot":60,
    "apple":50
}
print("initial ss mart",ss_mart)

ss_mart["eggs"]=10
ss_mart["musroom"]=40
print("updated ss mart",ss_mart)

ss_mart["orange"]=ss_mart["orange"]+5
ss_mart["musroom"]=ss_mart["musroom"]+5
print("after restocking",ss_mart)

del ss_mart["apple"]
print(ss_mart)



is_carrot_in_ss_mart="carrot"in ss_mart
print("is carrot in ss mart",is_carrot_in_ss_mart)
is_guava_in_ss_mart="guava"in ss_mart
print("is guava in ss mart",is_guava_in_ss_mart)

for product,product_count in ss_mart.items():
    print("product ",product,"is",product_count)
print(len(ss_mart))

print(ss_mart.items())
item,item_value="apple",20
print(item,item_value)

for val in ss_mart.items():
    print(val)
    print(type(val))

new_ss_mart={
    "apple":
    {
        "yesterday":10,
        "today":20
    }
}
print(new_ss_mart)



print(new_ss_mart.items())

a=["aruna",{},2,True]
print(a)
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(isinstance(a[0],str))


new_store=(new_ss_mart+ss_mart)
print(new_store)