def setMatrixZero(matrix):
    m=len(matrix)
    n=len(matrix[0])
    RowisZero=any(matrix[i][0]==0 for i in range(m))
    colisZero=any(matrix[0][j]==0 for j in range(n))


    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0

    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
    
    if RowisZero:
        for j in range(n):
            matrix[0][j]=0
    if colisZero:
        for i in range(m):
            matrix[i][0]=0
    return matrix

print(setMatrixZero([[1,1,1],[1,0,1],[1,1,1]]))