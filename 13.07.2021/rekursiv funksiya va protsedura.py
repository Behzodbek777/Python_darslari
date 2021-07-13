# 1-masala. 10 dan birgachgacha sonlarni chiqarish
"""def chiqarish(x):
    if x == 1:
        print(x)
    else:
        print(x)
        chiqarish(x-1)

chiqarish(10)"""

# 2-masala. k dan n gacha chiqarish
"""def KdanNgacha(k,n):
    if n == k:
        print(k)
    else:
        print(k)
        KdanNgacha(k +1, n)

KdanNgacha(1, 10)"""

# 3- masala. Factorial

def fact(n):
    if n==1:
        return 1
    else:
        return n*(fact(n-1))

print(fact(5))