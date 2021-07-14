import math


def aylana(l):
    return lambda a: l/(2*math.pi)
x= aylana(6)
print((x(2)))