son=int(input("son kiriting="))
a=0
for i in range(1, son + 1):
    if son%i==0:
        a += i
print(a)