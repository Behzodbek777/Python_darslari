n = int(input("n="))
def rim(n):
    yuz= n//100
    un= (n % 100) //10
    bir = n % 10
    d=yuz+un+bir
    return d
print(rim(n))