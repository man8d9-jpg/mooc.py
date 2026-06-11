def transpose(matrix: list):
    transpose = []
    for i in matrix:
        transpose.append(i[:])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transpose[j][i] = matrix[i][j]
        
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = transpose[i][j]
    
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose(matrix)
print(matrix)