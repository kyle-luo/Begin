# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.count = [0]
        if root is not None:
            self.deepcount(root, 0)
        return max(self.count)

    def deepcount(self, node, count):
        count += 1
        if node.left is not None or node.right is not None:
            if node.left is not None:
                self.deepcount(node.left, count)
            if node.right is not None:
                self.deepcount(node.right, count)
        else:
            self.count.append(count)


class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        self.longest = 0
        if root is not None:
            self.deepcount(root, 0)
        return self.longest

    def deepcount(self, node, count):
        count += 1
        if count > self.longest:
            self.longest = count
        if node.left is not None:
            self.deepcount(node.left, count)
        if node.right is not None:
            self.deepcount(node.right, count)


class Solution3:
    def maxDepth(self, root: TreeNode) -> int:
        self.longest = 0
        if root is not None:
            self.deepcount(root, 0)
        return self.longest

    def deepcount(self, node, count):
        count += 1
        if node.left is not None or node.right is not None:
            if node.left is not None:
                self.deepcount(node.left, count)
            if node.right is not None:
                self.deepcount(node.right, count)
        else:
            if count > self.longest:
                self.longest = count
