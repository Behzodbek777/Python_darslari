import random
b=[]
x=int(input("sonlar sonini kiriting:"))
y=int(input("boshlanish nuqtasini kiriting:"))
z=int(input("tugash nuqtasi kiriting:"))
i= 1
for i in range(x):
    b.append(random.randint(y,z))
print(b)
b=set(b)
print(len(b))
print(b)
