"""import os

if not os.path.exists("Baza.txt"):
    f = open("Baza.txt", "x")"""
n = int(input("xodimlar sonini kiriting:"))
for i in range(n):
    f = open("Baza.txt", "a")
    f.write(f"{i + 1} - xodim: \n")
    print(i + 1, "-xodim ma'lumotlarini kiriting:")
    ism = input("ismi:")
    f.write(f"{ism}\n")
    fam = input("familiya:")
    f.write(f"{fam}\n")

    print("\n")

    f.close()
f = open("Baza.txt", "r")
print(f.read())
