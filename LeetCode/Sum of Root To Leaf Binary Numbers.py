# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
#
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
#
# Return the sum of these numbers.
#
# Example 1:
#
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.collection = []
        if root is not None:
            self.get(root, '')
            result = 0
            for binary in self.collection:
                result += int(binary, 2)
            return result
        return None

    def get(self, node, cur):
        cur = cur + str(node.val)
        if node.left is not None:
            self.get(node.left, cur)
        if node.right is not None:
            self.get(node.right, cur)
        if node.left is None and node.right is None:
            self.collection.append(cur)