def printMatrix(matrix):
    print()
    for i in range(len(matrix)):
        s=''
        for j in range(len(matrix[i])):
            s+=str(matrix[i][j])+'\t'
        print(s)
        print()

n = int(input('Введите число строк и столбцов: '))
M = [[0]*n for i in range(n)]
ogr = n
index = 0
number = 0
while ogr>0:
    for i in range(ogr):
        number+=1
        M[index][i]=number
    index = i
    ogr-=1
    for i in range(ogr):
        number+=1
        M[i][index]=number
    index = i
    for i in range(ogr, 0, -1):
        number+=1
        M[index][i]=number
    index = i
    ogr-=1
    for i in range(ogr, 0,-1):
        number+=1
        M[i][index]=number
    index = i





printMatrix(M)


