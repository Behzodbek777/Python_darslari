ism=input("ism kiriting:")
if ism[-1]=="a" or ism[-1]=="e" or ism[-1]=="i" or ism[-1]=="o" or ism[-1]=="u":
    ism +="yev"
    print(ism)
elif ism[-1]=="f":
    ism = ism.replace(ism[-1], "p")
    ism+="ov"
    print(ism)
else:
    ism+="ov"
    print(ism)