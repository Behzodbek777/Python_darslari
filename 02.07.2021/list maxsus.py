royxat = ["ferrari", "chevrolet", "lexus", "malibu", "Rolls Royce", "BMW", "Daewo", "Ravon"]
a=(input("qiymat kiriting:"))
b=int(input("indeks kiriting:"))
c=len(royxat)
i=1
j=1
e=royxat[c-1]
r=c-1
for  i in range(r):
    if i<b:
        continue
    else:
        royxat[c-(j)]=royxat[c-(j+1)]
    i+=1
    j+=1
royxat[b]=a
royxat.append(e)
print(royxat)