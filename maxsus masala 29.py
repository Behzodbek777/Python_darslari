#maxsus masala. 29.06.2021 sanasidagi
while True:
    name=str(input("ism kiriting:"))
    a=name.split()
    if len(a)==1:
        break
    else:
        print("ism bir so'zdan iborat bo'lsin. qaytadan kiriting!")

while True:
    grandFatherName=str(input("boboning ismini kiriting:"))
    b = grandFatherName.split()
    if len(b) == 1:
        break
    else:
        print("ism bir so'zdan iborat bo'lsin. qaytadan kiriting!")

while True:
    fathername=str(input("dadaning ismini kiriting:"))
    c = fathername.split()
    if len(c) == 1:
        break
    else:
        print("ism bir so'zdan iborat bo'lsin. qaytadan kiriting!")

while True:
    jins = str(input("jinsni kiriting:"))
    d = jins.split()
    if jins == "erkak" or jins == "ayol":
        break
    else:
        print("jins faqat 'erkak' yoki 'ayol' bo'lishi kerak")

if jins == "ayol":

    if grandFatherName[-1]=="a" or grandFatherName[-1]=="e" or grandFatherName[-1]=="i" or grandFatherName[-1]=="o" or grandFatherName[-1]=="u":
        grandFatherName += "yeva"
    elif grandFatherName == "f":
        grandFatherName=grandFatherName[-1].replace("p")+"ova"
    else:
        grandFatherName += "ova"
    if fathername[-1] == "a" or fathername[-1] == "e" or fathername[-1] == "i" or fathername[-1] == "o" or grandFatherName[-1] == "u":
        fathername += "yevna"
    elif fathername == "f":
        fathername=fathername[-1].replace("p") + "ovna"
    else:
        fathername += "ovna"
    print(f"{grandFatherName} {name} {fathername}")
else:
    if grandFatherName[-1] == "a" or grandFatherName[-1] == "e" or grandFatherName[-1] == "i" or grandFatherName[-1] == "o" or grandFatherName[-1] == "u":
        grandFatherName += "yev"
    elif grandFatherName == "f":
        grandFatherName = grandFatherName[-1].replace("p") + "ov"
    else:
        grandFatherName += "ov"
    if fathername[-1] == "a" or fathername[-1] == "e" or fathername[-1] == "i" or fathername[-1] == "o" or grandFatherName[-1] == "u":
        fathername += "yevich"
    elif fathername == "f":
        fathername = fathername[-1].replace("p") + "ovich"
    else:
        fathername += "ovich"
    print(f"{grandFatherName} {name} {fathername}")
