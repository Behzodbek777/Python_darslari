sonlar=[2,8,4,5,4,1,2,6,9,0]
for index in range(len(sonlar)):
    for key in range(len(sonlar)):
        if sonlar[index] < sonlar[key]:
            sonlar[index] = sonlar[index] + sonlar[key]
            sonlar[key]= sonlar[index] - sonlar[key]
            sonlar[index]= sonlar[index] - sonlar [key]
print(sonlar)


