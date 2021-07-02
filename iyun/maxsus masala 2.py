#berilgan xonadagi sonni boshiga chiqarish
son=int(input("sonni kiriting="))
berilganXona1=int(input("berilgan xona raqamini kiriting:"))
a=son


xonalarSoni=1
while True:
    a=a//10
    if a!=0:
        xonalarSoni+=1
    else:
        break
"""print(xonalarSoni)"""
if berilganXona1 <= xonalarSoni:
    berilganXona=berilganXona1+1
    son1=son//(10**(xonalarSoni-(berilganXona-1)))
    son2=son1%10
    son3=son1//10
    son4=son%(10**(xonalarSoni-(berilganXona-1)))
    javob=son2*10**(xonalarSoni-1)+son3*10**(xonalarSoni-berilganXona+1)+son4
    print(javob)
else:
    print("bunday xona yo'q")