def antisymmetric(A):
    #Write your code here
    if A == [[]] or []:
        return True
    else:
        if len(A) == len(A[0]):
            n = len(A)
            x = 0
            y = 0
            while x < n:
                if x == y:
                    x += 1
                elif A[x][y] == -A[y][x]:
                    y = 0
                    while y < n:
                        if x == y:
                            y += 1
                        elif A[x][y] == -A[y][x]:
                            y += 1
                        else:
                            return False
                    x += 1
                else:
                    return False
                y = 0

            return True
        else:
            return False
