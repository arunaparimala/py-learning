
try:
    i=1
    while(i<100):
       print(i)
       i=i+10
       print(i%2)
       print(i%0)
       
except Exception:
    print("zerodivision error as e")

finally:
    print("done")
print(i%1)
