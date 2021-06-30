x=int(input("x="))
y=int(input("y="))
ekuk=1
while True:
    if ekuk%x==0 and ekuk%y==0:
        break
    ekuk+=1
print(ekuk)
