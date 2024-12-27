#opening file
with open("ello.py","r")as file:
    print(file,type(file))

#reading file
with open("ello.py","r")as file:
    content=file.readlines()
    print(content)
    for line in content:
        print(line)

#writing to a file
with open("notes.txt","w")as file:
    file.write("welcome perinba  \n")
    file.write("go to scool\n")

#appending file
with open("notes.txt","a")as file:
    file.write("be appy forever\n")

#cecking file existance
import os

if os.path.isfile("odd.py"):
    print("odd.py found")
else:
    print("not found")

with open("odd.py","r")as odd_file:
    content=odd_file.readlines()
    print(content)
for details in content:
    print(details)

#working wit binary files
with open("map.bin","rb")as file:
    details=file.read()
    print(details)

#deleting file
import os

os.remove("secrets.txt")