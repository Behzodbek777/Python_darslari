oquchilar = ["Abduvaliyeva", "Abdusalomova", "Aliqulova", "Jabborov", "Sattorov", "Xudoyorov" ]
print(oquchilar)
oquchilar.append("Xudoyberdiyev")
print(oquchilar)
oquchilar.insert(3,"Bo'ribekova")
print(oquchilar)
print(len(oquchilar))
oquchilar.append("Aliqulova")
print(oquchilar.count("Aliqulova"))
oquchilar1 = ["Boboyeva", "Ro'ziqulov", "Jo'rayeva"]
oquchilar.extend(oquchilar1)
print(oquchilar)
print(oquchilar.index("Jo'rayeva"))
oquchilar.clear()
print(oquchilar)