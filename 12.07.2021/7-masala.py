a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))
e=int(input("e="))
def EngKat(a,b,c,d,e):
    katta=max(a,b,c,d,e)
    return katta
def EngKich(a,b,c,d,e):
    kichik = min(a, b, c, d, e)
    return kichik
def urtacha(a,b,c,d,e):
    urtaAr=((a+b+c+d+e)-EngKat(a,b,c,d,e)-EngKich(a,b,c,d,e))/3
    return urtaAr

print(f"{EngKich(a,b,c,d,e)} {EngKat(a,b,c,d,e)}")
print(urtacha(a,b,c,d,e))