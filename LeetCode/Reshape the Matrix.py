# In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
#
# You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.
#
# The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.
#
# If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
#
# Example 1:
# Input:
# nums =
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# Output:
# [[1,2,3,4]]
# Explanation:
# The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
#
# Example 2:
# Input:
# nums =
# [[1,2],
#  [3,4]]
# r = 2, c = 4
# Output:
# [[1,2],
#  [3,4]]
# Explanation:
# There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if sum(len(x) for x in nums) != r * c:
            return nums
        else:
            output = [[]]
            for x in nums:
                for num in x:
                    if len(output[-1]) < c:
                        output[-1].append(num)
                    else:
                        output.append([])
                        output[-1].append(num)
            return output


import queue
class Solution2:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
        else:
            q = queue.Queue()
            for x in nums:
                for num in x:
                    q.put(num)
            output = [[None for _ in range(c)] for _ in range(r)]
            for i in range(r):
                for j in range(c):
                    output[i][j] = q.get()
            return output


class Solution3:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        M, N = len(nums), len(nums[0])
        if M * N != r * c:
            return nums
        else:
            res = [[0] * c for _ in range(r)]
            row, col = 0, 0
            for i in range(M):
                for j in range(N):
                    if col == c:
                        row += 1
                        col = 0
                    res[row][col] = nums[i][j]
                    col += 1
            return res