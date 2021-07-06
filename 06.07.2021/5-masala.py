a=(1,2,3,4,5,6)
b=list(a)
for i in range(len(b)):
    if i+1%2==0:
        b[i]=b[i]**2
        print(b[i])
    i+=1