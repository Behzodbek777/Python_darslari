#ro'yxatni istalgan indeksiga istalgan elementni kiritish algoritmi:
royxat = ["ferrari", "chevrolet", "lexus", "malibu", "Rolls Royce", "BMW", "Daewo", "Ravon"]
element=(input("qiymat kiriting:"))
indeks1=int(input("indeks kiriting:"))
uzunlik=len(royxat)
i=1
j=1
oxirgiElement=royxat[uzunlik-1]
r=uzunlik-1
for  i in range(r):
    if i<indeks1:
        continue
    else:
        royxat[uzunlik-(j)]=royxat[uzunlik-(j+1)]
    i+=1
    j+=1
royxat[indeks1]=element
royxat.append(oxirgiElement)
print(royxat)