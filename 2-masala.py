import math
a=int(input("tomonni kiritng:"))
b=int(input("tomonni kiriting:"))
c=int(input("tomonni kiriting:"))

p=(a+b+c)/2
S=pow(p*(p-a)*(p-b)*(p-c),1/2)
P=a+b+c
print(f"Ushburchakning yuzi:{S}")
print(f"Uchburchakning perimetri:{P}")