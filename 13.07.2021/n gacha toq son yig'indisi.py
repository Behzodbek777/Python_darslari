def toqSon(n):
    if n%2==1:
        if n == 1 or n ==0:
            return 1
        else:
            return n + toqSon(n - 2)
    else:
        n-=1
        return n + toqSon(n - 2)


print(toqSon(12))
