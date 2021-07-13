ism = input("isminggizni kiriting:")
try:
    a = 5 + ism
    print(f"salom {ism}")


except:
    if ism == "Behzod":
        print("bu boshqa ism ")
    print("dasturda xato")
finally:
    if ism =="Behzod":
        print("dastur to'g'ri")
    else:
        print("Boshqa ism kiriting:")
