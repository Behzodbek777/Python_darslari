try:
    x = int(input("x="))
    if x % 2 == 0:
        raise Exception("juft son kiritish mumkin emas")
except:
    print("juft son kiritish mumkin emas")
else:
    print("siz to'g'ri kirittinggiz")
finally:
    print("dastur tugadi")