import random

A = []
B = []
C = []
for i in range(10):
    A.append(random.randint(1, 10))
    B.append(random.randint(1, 10))
    C.append(random.randint(1, 10))
A = set(A)
B = set(B)
C = set(C)

print(A)
print(B)
print(C)
A.update(B)
print(f"A va B ning yig'indisi:{A}")
A.intersection_update(C)
print(f"A va B ning yig'indisiga C ning ko'paytmasi:{A}")
