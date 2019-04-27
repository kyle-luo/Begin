# Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].
#
# After this process, we have some array B.
#
# Return the smallest possible difference between the maximum value of B and the minimum value of B.
#
#
#
# Example 1:
#
# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]
# Example 2:
#
# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]
# Example 3:
#
# Input: A = [1,3,6], K = 3
# Output: 0
# Explanation: B = [3,3,3] or B = [4,4,4]

def smallestRangeI(A, K):
    big, small = max(A) - K, min(A) + K
    if big > small:
        return big - small
    return 0

print(smallestRangeI([0,10],2))


def smallestRangeI(A, K):
    biggest = A[0]
    smallest = A[0]
    for x in A:
        if x > biggest:
            biggest = x
        elif x < smallest:
            smallest = x
    big = biggest - K
    small = smallest + K
    return max(0, big - small)

print(smallestRangeI([0,10],2))

def smallestRangeI(A, K):
    res = max(A) - min(A)
    return res - K * 2 if res > K * 2 else 0

print(smallestRangeI([0,10],2))