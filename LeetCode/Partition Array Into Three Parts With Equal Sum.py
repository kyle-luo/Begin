# Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.
#
# Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])
#
#
#
# Example 1:
# Input: [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

# Example 2:
# Input: [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false

# Example 3:
# Input: [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        goal = sum(A) / 3
        count = 0
        cur_v = 0
        for i, x in enumerate(A):
            if cur_v == goal:
                count += 1
                cur_v = 0
            cur_v += x
        if count == 2 and cur_v == goal:
            return True
        elif count == 3 and cur_v == 0:
            return True
        else:
            return False

class Solution2:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        goal = sum(A) / 3
        count = 0
        cur_v = 0
        for i, x in enumerate(A):
            cur_v += x
            if cur_v == goal:
                count += 1
                cur_v = 0
            if count == 2:
                if i < len(A) - 1:
                    if sum(A[i+1:]) == goal:
                        return True
                    return False
                return True