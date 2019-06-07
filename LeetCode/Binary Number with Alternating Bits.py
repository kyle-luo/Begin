# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
#
# Example 1:
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
# Example 2:
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
# Example 3:
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
# Example 4:
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.
#

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bi = bin(n)[2:]
        i = 0
        while i < len(bi):
            if bi[i] != '1':
                return False
            i += 2
        j = 1
        while j < len(bi):
            if bi[j] != '0':
                return False
            j += 2
        return True


class Solution2:
    def hasAlternatingBits(self, n: int) -> bool:
        bi = bin(n)[2:]
        pre = bi[0]
        for i in range(1, len(bi)):
            if bi[i] == pre:
                return False
            pre = bi[i]
        return True