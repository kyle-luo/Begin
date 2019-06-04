# Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.
#
# If there aren't two consecutive 1's, return 0.
#
# Example 1:
# Input: 22
# Output: 2
# Explanation:
# 22 in binary is 0b10110.
# In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
# The first consecutive pair of 1's have distance 2.
# The second consecutive pair of 1's have distance 1.
# The answer is the largest of these two distances, which is 2.
#
# Example 2:
# Input: 5
# Output: 2
# Explanation:
# 5 in binary is 0b101.
#
# Example 3:
# Input: 6
# Output: 1
# Explanation:
# 6 in binary is 0b110.
#
# Example 4:
# Input: 8
# Output: 0
# Explanation:
# 8 in binary is 0b1000.
# There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.

class Solution:
    def binaryGap(self, N: int) -> int:
        num = list(bin(N))
        num.pop(0)
        num.pop(0)
        max = 0
        if len(num) > 1:
            pre = num.index('1')
            for i in range(len(num)):
                if num[i] == '1':
                    temp = i - pre
                    pre = i
                    if temp > max:
                        max = temp
        return max


class Solution2:
    def binaryGap(self, N: int) -> int:
        num = bin(N)
        max = 0
        pre = num.find('1')
        while True:
            gap = num[pre + 1:].find('1') + 1
            if gap == 0:
                break
            if gap > max:
                max = gap
            pre += gap
        return max


class Solution3:
    def binaryGap(self, N: int) -> int:
        count = []
        for i, j in enumerate(bin(N)):
            if j == '1':
                count.append(i)
        if len(count) < 2:
            return 0
        return max(count[i] - count[i - 1] for i in range(1, len(count)))