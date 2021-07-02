import math

x = int(input("x=:"))
y = int(input("y="))
a = int(input("a="))
G = (math.cos(2 * abs(y + x) - (x + y)) ** (4 * x ** 2)) / ((math.atan(x + a) ** 4) * x ** 5)
print(G)
