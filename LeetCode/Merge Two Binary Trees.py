# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
#
# Example 1:
#
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is not None and t2 is not None:
            t1.val += t2.val
            def _merge(self, t1, t2):
                if t1.left is not None and t2.left is not None:
                    t1.left.val += t2.left.val
                    _merge(self, t1.left, t2.left)
                elif t1.left is None and t2.left is not None:
                    t1.left = TreeNode(t2.left.val)
                    _merge(self, t1.left, t2.left)
                if t1.right is not None and t2.right is not None:
                    t1.right.val += t2.right.val
                    _merge(self, t1.right, t2.right)
                elif t1.right is None and t2.right is not None:
                    t1.right = TreeNode(t2.right.val)
                    _merge(self, t1.right, t2.right)
            _merge(self, t1, t2)
        elif t1 is None and t2 is not None:
            t1 = TreeNode(t2.val)
        return t1


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is not None and t2 is not None:
            t1.val += t2.val
            self._merge(t1, t2)
        elif t1 is None and t2 is not None:
            t1 = TreeNode(t2.val)
            self._merge(t1, t2)
        return t1

    def _merge(self, t1, t2):
        if t1.left is not None and t2.left is not None:
            t1.left.val += t2.left.val
            self._merge(t1.left, t2.left)
        elif t1.left is None and t2.left is not None:
            t1.left = TreeNode(t2.left.val)
            self._merge(t1.left, t2.left)
        if t1.right is not None and t2.right is not None:
            t1.right.val += t2.right.val
            self._merge(t1.right, t2.right)
        elif t1.right is None and t2.right is not None:
            t1.right = TreeNode(t2.right.val)
            self._merge(t1.right, t2.right)