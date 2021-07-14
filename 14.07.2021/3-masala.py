def ism(n):

    return lambda a: n*a
n=input("n=")
a=int(input("a="))
x=ism(n)
print(x(a))