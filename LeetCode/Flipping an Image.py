# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
#
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
#
# Example 1:
#
# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:
#
# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

def flipAndInvertImage(A):
    finalresult = []
    for list in A:
        tempresult = []
        for a in list:
            if a == 1:
                tempresult.insert(0,0)
            elif a == 0:
                tempresult.insert(0,1)
        finalresult.append(tempresult)
    return finalresult

print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

def flipAndInvertImagee(A):
    finalresult = []
    start = 0
    for list in A:
        finalresult.append([])
        for a in list:
            if a == 1:
                finalresult[start].insert(0,0)
            elif a == 0:
                finalresult[start].insert(0,1)
        start += 1
    return finalresult

print(flipAndInvertImagee([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

def flipAndInvertImageee(A):
    for list in A:
        for num in range(int((len(list)+1)/2)):
            list[num], list[~num] = list[~num]^1, list[num]^1
    return A

print(flipAndInvertImageee([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

