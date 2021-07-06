a=(1,2,3,4,5,6)
i=0
b=list(a)
c=[]
while i<(len(a)//2):
    if i==0:
        c.append(b[0])
    else:
        c.append(b[-i])
        c.append(b[i])
    i += 1
else:
    c.append(b[i])
print(c)