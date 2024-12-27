stationary={
    "pen":10,
    "pencil":20,
    "notebook":25,
    "eraser":70
}
print(stationary)

for key in stationary:
    print(key, stationary.get(key))

for val in stationary.items():
    print(val)

print(list(stationary.keys()))
print(list(stationary.values()))

print(len(stationary))
stationary["stapler"]=50
print(stationary)

while(6<= 10):
    stationary["paper"]=24

    if len(stationary)<=6:
      print(stationary)
      break

