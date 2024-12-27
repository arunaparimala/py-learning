import time
for i in range(1,13):
    time.sleep(3)
    print(i)
    for j in range(i):
        print(i,end='-')
        exit(0)