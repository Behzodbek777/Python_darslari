B = [[[],[]], [[],[]]]
for i in range(2):
    for j in range(2):
        B[i][j]=int(input(f"{B[i][j]}="))
print(B)
for i in B:
    for j in i:
        print(j)