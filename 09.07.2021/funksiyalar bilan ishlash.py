"""def salom():
    print("Hello World")
salom()
nom = input()"""
"""def ism(name):

    print(f"Salom {name}")
ism(nom)
"""
"""son=int(input("son kiriting:"))
def ikkilangan(x):
    print(x*2)
ikkilangan(son)"""
"""ko'p parametrli funksiya"""
"""def toliq_ism(ism, familiya):
    tuliq = ism + " " + familiya
    print(tuliq)
toliq_ism("Behzod", "Abdushukurov")
toliq_ism("Ulug'bek", "Abdushukurov")"""


"""*args -> bu nomalum parametrlar to'plami"""
"""def ismlarRoyxati(*ism):
    print(ism)
ismlarRoyxati("Behzod", "Azizbek", "Ulug'bek", "Muhammadshokir")"""


"""def fanlarRoyxati(fan):
    print(list(fan))
b=[]
for i in range(6):
    a= input("fan kiriting")
    b.append(a)
fanlarRoyxati(b)"""

"""#keyword -> kalit so'z

def ismFamiliya(ism, familiya):
    print(f"{ism} {familiya}")

ismFamiliya("Behzod", "Abdushukurov")"""

#ko'p kalit so'zlardan foydalanish
"""def uquvchi(**x):
    print(x)
uquvchi(ism = "Behzod", familiya= "Abdushukurov", yoshi = 25)"""

def YoqtirganRang(rang="qora"):
    print(f" men {rang} rangni yoqtiraman")


YoqtirganRang()