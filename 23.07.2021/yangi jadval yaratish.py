import mysql.connector

meningBMB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jizzax*96",
    database="maktab"
)

mycursor = meningBMB.cursor()
# mycursor.execute("""
# create table ismlar
# (ism varchar(50))""")
print("--Ismlar jadvali--")
print("1. Jadvalni ko'rish")
print("2. ism qo'shish")
print("3. ismni o'zgartirish")
print("4. ismni o'chirish")
print("0. chiqish")

while True:
    n = int(input("kerakli raqamni tanlang: "))

    if n == 1:
        print("ismlar ro'yxati:\n")

        mycursor.execute("select ism from ismlar")
        for i in mycursor:
            print(i)
    elif n == 2:
        ism = input("ism kiriting: ")
        mycursor.execute(f"insert into ismlar values ('{ism}')")
        meningBMB.commit()
    elif n == 3:

        eski_ism = input("o'zgartiriladigan ismni kiriting: ")
        mycursor.execute("select *from ismlar")
        ismlar = []
        for i in mycursor:
            ismlar.append(i[0])
        if eski_ism in ismlar:
            yangi_ism = input("yangi ismni kiriting: ")
            mycursor.execute(f"update ismlar set ism='{yangi_ism}' where ism='{eski_ism}' ")
            meningBMB.commit()
        else:
            print("bumday ism yo'q")
    elif n == 4:



    elif n == 0:
        break

