# 3- masala
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]
matrix3 = [[matrix1[0][0]+matrix2[0][0],matrix1[0][1]+matrix2[0][1]],[matrix1[1][0]+matrix2[1][0],matrix1[1][1]+matrix2[1][1]] ]
print(matrix3)
for i in range(2):
    for j in range(2):

        matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
print(matrix3)