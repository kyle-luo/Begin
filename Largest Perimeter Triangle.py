# Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
#
# If it is impossible to form any triangle of non-zero area, return 0.
#
#
#
# Example 1:
#
# Input: [2,1,2]
# Output: 5
# Example 2:
#
# Input: [1,2,1]
# Output: 0
# Example 3:
#
# Input: [3,2,3,4]
# Output: 10
# Example 4:
#
# Input: [3,6,2,3]
# Output: 8

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        A.sort()
        sides = []
        while len(sides) < 3 and len(A) > 0:
            sides.append(A.pop())
            if len(sides) == 3:
                if sides[0] - sides[1] - sides[2] < 0:
                    return sum(sides)
                else:
                    sides.pop(0)
        return 0


class Solution2:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        i = len(A) - 1
        while i >= 2:
            if A[i] - A[i - 1] - A[i - 2] < 0:
                return A[i] + A[i - 1] + A[i - 2]
            i -= 1
        return 0