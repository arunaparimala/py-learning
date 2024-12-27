import json
a="""{"name":"perinba","age":2}"""
print(a)
b=json.loads(a)
print(b)
c=json.dumps(a)
print(c)

with open("ello.json","w")as file:
    file.write()

with open("ello.json","r")as file:
    details=file.read()
    print(details)