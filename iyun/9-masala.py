x = int(input("x="))
y = int(input("y="))
l = ((x ** 2) + (y ** 2)) ** (1 / 2)
if l == 4:
    if x==0:
        print("nuqta aylana chegarasida va y o'qida yotadi yotadi")
    elif y==0:
        print("nuqta aylana chegarasida va x o'qida yotadi yotadi")
elif l > 4:
    if x > 0 and y > 0:
        print("nuqta aylana tashqarisida yotadi ")
        print("nuqta birinchi chorakda yotadi ")

    elif x < 0 and y > 0:
        print("nuqta aylana tashqarisida yotadi ")
        print("nuqta ikkinchi chorakda yotadi ")
    elif x < 0 and y < 0:
        print("nuqta aylana tashqarisida yotadi ")
        print("nuqta uchinchi chorakda yotadi ")
    elif x > 0 and y < 0:
        print("nuqta aylana tashqarisida yotadi ")
        print("nuqta ikkinchi chorakda yotadi ")
elif l < 4 and y == 0:
    print("nuqta aylana ichkarisida va x o'qida yotadi ")
elif l < 4 and x == 0:
    print("nuqta aylana ichkarisida va y o'qida yotadi ")
elif l < 4 :

    if x>0 and y>0:
        print("nuqta aylana ichkarisida yotadi ")
        print("nuqta birinchi chorakda yotadi ")

    elif x < 0 and y > 0:
        print("nuqta aylana ichkarisida yotadi ")
        print("nuqta ikkinchi chorakda yotadi ")
    elif x < 0 and y < 0:
        print("nuqta aylana ichkarisida yotadi ")
        print("nuqta uchinchi chorakda yotadi ")
    elif x > 0 and y < 0:
        print("nuqta aylana ichkarisida yotadi ")
        print("nuqta ikkinchi chorakda yotadi ")
elif l == 0:
    print("nuqta koordinata boshida yotadi")
print(l)