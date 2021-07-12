n= int(input("n="))
i=1
def kvadrat(n):
     qiymat=[]
     for i in range(1,n):
        if i**2 < n:
            qiymat.append(i)
     return qiymat
print(kvadrat(n))


