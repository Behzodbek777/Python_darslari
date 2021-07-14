def hajm(a, b):
    return lambda c: (a + b) ** c


yuza = hajm(5, 3)
print(yuza(4))
