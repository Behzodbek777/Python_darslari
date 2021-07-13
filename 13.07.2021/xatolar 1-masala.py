try:
    a = int(input("a="))
    if a < 0:
        raise Exception("manfiy son kiritish mumkin  emas")
    

except:
    print("siz manfiy son kirittingiz. Iltimos faqat musbat son kiriting!")
else:
    print("yaxshi siz musbat son kirittingiz")
