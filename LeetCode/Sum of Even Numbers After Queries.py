# We have an array A of integers, and an array queries of queries.
#
# For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.
#
# (Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)
#
# Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.
#
#
#
# Example 1:
#
# Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
# Explanation:
# At the beginning, the array is [1,2,3,4].
# After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
# After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
# After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
# After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

def sumEvenAfterQueries(A, queries):
    result = []
    for x in queries:
        A[x[1]] += x[0]
        esum = 0
        for x in A:
            if x % 2 == 0:
                esum += x
        result.append(esum)
    return result

print(sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))

def sumEvenAfterQueries(A, queries):
    orgsum = 0
    for x in A:
        if x % 2 == 0:
            orgsum += x
    result = []
    for x in range(len(queries)):
        if A[queries[x][1]] % 2 == 0:
            if queries[x][0] % 2 == 0:
                orgsum += queries[x][0]
                A[queries[x][1]] += queries[x][0]
                result.append(orgsum)
            else:
                orgsum -= A[queries[x][1]]
                A[queries[x][1]] += queries[x][0]
                result.append(orgsum)
        else:
            if queries[x][0] % 2 == 0:
                A[queries[x][1]] += queries[x][0]
                result.append(orgsum)
            else:
                orgsum += (A[queries[x][1]] + queries[x][0])
                A[queries[x][1]] += queries[x][0]
                result.append(orgsum)
    return result


print(sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))

def sumEvenAfterQueries(A, queries):
    orgsum = 0
    for x in A:
        if x % 2 == 0:
            orgsum += x
    result = []
    for x,y in queries:
        if A[y] % 2 == 0:
            orgsum -= A[y]
        A[y] += x
        if A[y] % 2 == 0:
            orgsum += A[y]
        result.append(orgsum)
    return result

print(sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]])) 