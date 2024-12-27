with open("list.py","r")as file:
    content=file.read()
    print(content)

with open("naturalnumbers.py","w")as nw:
    nw.write("for i in range(1,100):\n")
    nw.write("   print(i)\n")