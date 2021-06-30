a=int(input("a="))
b=int(input("b="))
i=2
while True:
    i+=2
    a+=i
    if a%2==0:
        break
    else:
        a+=1

    print(a)


