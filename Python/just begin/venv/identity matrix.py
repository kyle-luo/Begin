def is_identity_matrix(matrix):
    if matrix != [] or matrix != [[]]:
        if len(matrix) == len(matrix[0]):
            n = len(matrix)
            x = 0
            while x < n:
                if matrix[x][x] == 1:
                    y = 0
                    while y < n:
                        if matrix[x][y] == matrix[y][x]:
                            y += 1
                        else:
                            return False
                else:
                    return False
                x += 1
        else:
            return False
        return True
    else:
        return True





matrix1 = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]
print is_identity_matrix(matrix1)
# >>>True

matrix2 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 0]]

print is_identity_matrix(matrix2)
# >>>False

matrix3 = [[2, 0, 0],
           [0, 2, 0],
           [0, 0, 2]]

print is_identity_matrix(matrix3)
# >>>False

matrix4 = [[1, 0, 0, 0],
           [0, 1, 1, 0],
           [0, 0, 0, 1]]

print is_identity_matrix(matrix4)
# >>>False

matrix5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

print is_identity_matrix(matrix5)
# >>>False

matrix6 = [[1, 0, 0, 0],
           [0, 1, 0, 1],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]

print is_identity_matrix(matrix6)
# >>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
# >>>False
