n=int(input("n="))
def boluvchilar(n):
    a=""
    for i in range(1, n+1):
        if n%i==0:
            a += str(i) + ' '
    print(f"{a}")
boluvchilar(n)