# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
#
# The binary search tree is guaranteed to have unique values.
#
#
#
# Example 1:
#
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# Example 2:
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.su = 0
        def s(cur):
            if L <= cur.val <= R:
                self.su += cur.val
            if cur.left is not None:
                s(cur.left)
            if cur.right is not None:
                s(cur.right)
        s(root)
        return self.su


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        input = [root]
        while input:
            cur = input.pop()
            if L <= cur.val <= R:
                sum += cur.val
            if cur.left is not None:
                input.append(cur.left)
            if cur.right is not None:
                input.append(cur.right)
        return sum


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        input = [root]
        while input:
            cur = input.pop()
            if cur:
                if L <= cur.val <= R:
                    sum += cur.val
                if L < cur.val:
                    input.append(cur.left)
                if R > cur.val:
                    input.append(cur.right)
        return sum