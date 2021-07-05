olcham=int(input("olchamni kiriting:"))
a=[[0]*olcham]*olcham

print(a)
for i in range(olcham):
    for j in range(olcham):
        a[i][j]= (input(f"a{[i]}{[j]}="))
print(a)

