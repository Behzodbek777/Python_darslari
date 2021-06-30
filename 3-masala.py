import math
a=int(input("tomonni kiritng:"))
b=int(input("tomonni kiriting:"))
burchak=int(input("burhakni  kiriting:"))
c=(a**2+b**2-2*a*b*math.cos(burchak/180*math.pi))**(1/2)
print(c)