import json
with open("/home/aruna/Downloads/example_2.json","r")as file:
    data=json.load(file)
    print(data)

# with open("/home/aruna/Downloads/example_2.json","r")as file:
#     json.dump(d

print(type(data))
print(data.get("maths"))
print(list(data))

print(data.items())
print(type(data))
print(len(data))

for val in data.items():
    print(val)
    print(type(val))

is_quiz_in_data="quiz"in data
print(is_quiz_in_data)

is_q1_in_data="q1" in data
print("q1",is_q1_in_data)

for key in data:
    print(key,data.get(key))

for quiz in data:
    print(quiz)

for line in data[quiz]:
    
       print(line)
print()

for q1 in data.get(key):
    print(q1)


for key,value in data.items():
    if key=="sport":
       print("key",key,"value",value)

for values in data.values():
    print(values)

for key in data:
    value=data[key]
    
    print(f"key:{key},value:{value}")
    print()
 
for i in data:
    print(data[i])
    print(data[i].keys())
    if data[i]=="q1":
        print(data[i].keys())

    print(data[i].values()) 

print(data[i].get("sport"))
print(data[i].get("maths"))


print(data[i].clear())
print(data)




    




    
    