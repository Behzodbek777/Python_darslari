"""def fibonachi(n):
    if n==1:
        print(1)
    if n==2:
        print(1)
        print(1)
    else:

fibonachi(2)"""
n = int(input("n="))
a = []
a.append(1)
a.append(1)
for i in range(n):
    if i > 1:
        a.append(a[i - 1] + a[i - 2])
    else:
        i += 1


def fibonachi(n):
    print(a)


fibonachi(n)
