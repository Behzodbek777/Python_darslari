#oxirgi xonadagi sonni boshiga chiqarish
son=int(input("son="))
a=son
xonalarSoni=1
while True:
    a=a//10
    if a!=0:
        xonalarSoni+=1
    else:
        break
"""print(xonalarSoni)"""
chalaSon=son//10
qoldiq=son%10
javob=qoldiq*10**(xonalarSoni-1)+chalaSon
print(javob)