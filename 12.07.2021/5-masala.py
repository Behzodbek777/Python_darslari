n = int(input("n="))
def rim(n):
    yuz= n//100
    un= (n % 100) //10
    bir = n % 10
    if yuz == 1:
        a = "C"
    elif yuz == 2:
        a = "CC"
    elif yuz == 3:
        a = "CCC"
    elif yuz == 4:
        a = "CD"
    elif yuz == 5:
        a = "D"
    elif yuz == 6:
        a = "DC"
    elif yuz == 7:
        a = "DCC"
    elif yuz == 8:
        a = "DCCC"
    elif yuz == 9:
        a = "CM"
    elif yuz == 0:
        a = ""
    if bir == 1:
        x = "I"
    elif bir == 2:
        x = "II"
    elif bir == 3:
        x = "III"
    elif bir== 4:
        x = "IV"
    elif bir == 5:
        x = "V"
    elif bir == 6:
        x = "VI"
    elif bir == 7:
        x = "VII"
    elif bir == 8:
        x = "VIII"
    elif bir == 9:
        x = "IX"
    elif bir == 0:
        x = ""
    if un== 1:
        c = "X"
    elif un == 2:
        c = "XX"
    elif un == 3:
        c = "XXX"
    elif un == 4:
        c = "XL"
    elif un == 5:
        c = "L"
    elif un == 6:
        c = "LX"
    elif un == 7:
        c = "LXX"
    elif un == 8:
        c = "LXXX"
    elif un == 9:
        c = "XC"
    elif un == 0:
        c = ""
    print(str(a)+str(c)+str(x))
rim(n)
