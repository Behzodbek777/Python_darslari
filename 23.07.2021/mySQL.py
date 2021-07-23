import mysql.connector

meningBMB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jizzax*96",
    database="maktab"
)

cursor = meningBMB.cursor()


def jadvallar(a):
    cursor.execute("show tables")
    for i in a:
        print(i)


jadvallar(cursor)


def jadvallarni_korish(b):
    cursor.execute("select * from uqituvchilar")
    for j in b:
        print(j)


jadvallarni_korish(cursor)