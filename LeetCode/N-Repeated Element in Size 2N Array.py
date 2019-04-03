def repeatedNTimes(A):
    setA = set(A)
    for int in A:
        if A.count(int) == len(setA)-1:
            print int
            break

repeatedNTimes([1,2,3,3])