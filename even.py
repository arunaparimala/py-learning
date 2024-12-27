odd_count=0
even_count=0

for i in range(1,11):
    if(i%2==0):
        print(i)
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("even_count is",even_count)
print("odd_count is",odd_count)