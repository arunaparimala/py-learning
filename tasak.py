#using for loop in list
colors=["red","black","wite","yellow","red"]
print(colors.index("black"))
for val in colors:
    print (val)

#using wile loop in list
colors=["red","black","wite","yellow","red"]
colors.append("orange")
print(len(colors))

while(len(colors) <= 100):
    colors.append(1)
    if len(colors)<=10:
       print(colors)
       break



    
