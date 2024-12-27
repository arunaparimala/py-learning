a=[]
for i in range(10):
    num=input("enter num"+str(i+1))
    a.append(num)
print(a)


sum=0
for i in a:
    sum=sum+int(i)
print(sum)
ave=sum/10
print(ave)
