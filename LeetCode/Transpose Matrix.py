# Given a matrix A, return the transpose of A.
#
# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
#
#
#
# Example 1:
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
#
# Example 2:
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

def transpose(A):
    output = []
    for j in range(len(A[0])):
        tempout = []
        for i in range(len(A)):
            tempout.append(A[i][j])
        output.append(tempout)
    return output

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(transpose([[1,2,3],[4,5,6]]))

def transpose(A):
    output = [[''] * (len(A)) for x in range(len(A[0]))]
    for j in range(len(A[0])):
        for i in range(len(A)):
            output[j][i] = A[i][j]
    return output

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(transpose([[1,2,3],[4,5,6]]))

def transpose(A):
    return list(list(a) for a in zip(*A))

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(transpose([[1,2,3],[4,5,6]]))