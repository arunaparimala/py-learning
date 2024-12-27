message="welcome perinba"     #welcome perinba
print(message[3])              #01234567891011121314

print(message[-6])#negative indexing
print(message[7:16]) #start:stop:step

print(message[9:])
print(message[:17])
print(message[:7])
#negative indexing
print(message[-5:-7]) #print empty string .strimgs are movedon forward direction or step

print(message[-7:-5])

print(message[3:-8:1])

print(len(message))

print(message[-1:-5:-1])
print(message[-5:-1])

message="aruna"
print(message[0:3])
print(message[0:4:1])
print(message[0:4:2])

letters="welcome diwali"
for i in letters[1:8]:
   print(i)

#splitting metod
email="arunapari002@gmail.com"
print(email.split("@"))
