ismVaFamiliya = 0
yosh = 0
#manzil = str(input("manzilinggizni kiriting:"))
while True:
    ismVaFamiliya = str(input("ism va familiya kiriting:"))
    a=ismVaFamiliya.split()

    if len(a)==2:
        break
    else:
        print("ism va familiya alohida yozilishi kerak")
print(ismVaFamiliya)
while True:
    yosh = int(input("yoshinggiz nechida:"))
    if yosh >=18 :
        break
    else:
        print("18 yoshdan katta bo'lsin!")
print(yosh)
