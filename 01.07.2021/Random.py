import random
a=1
while a<=5:
    son = int(input("son="))
    if son == random.randint(1,10):
        print("Yuttinggiz")
        break

    else:
        print("qaytadan kiriting:")
    a+=1
else:
    print("yutkazdinggiz")