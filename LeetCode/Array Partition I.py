# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
#
# Example 1:
# Input: [1,4,3,2]
#
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].
def arrayPairSum(nums):
    sum = 0
    newnums = sorted(nums)
    for x in range(int(len(nums) / 2)):
        sum += newnums[2 * x]
    return sum
print(arrayPairSum([1,4,3,2]))


def arrayPairSumm(nums):
    newnums = sorted(nums)
    return sum(newnums[2 * x] for x in range(int(len(nums) / 2)))

print(arrayPairSumm([1,4,3,2]))

def arrayPairSummm(nums):
    return sum(sorted(nums)[::2])

