son = int(input("son kiriting:"))

i = 1
while True:
    chalaSon = son // 10
    sanoq = 1
    boluvchi = 10
    qoldiq = son % 10
    bolinma = son // boluvchi
    if bolinma == 0:
        javob = (10**i) * qoldiq + chalaSon
        print(javob)
        break


    i += 1
    sanoq *= 10
    boluvchi *= 10
