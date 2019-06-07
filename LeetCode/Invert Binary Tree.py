# Invert a binary tree.
# #
# # Example:
# #
# # Input:
# #
# #      4
# #    /   \
# #   2     7
# #  / \   / \
# # 1   3 6   9
# # Output:
# #
# #      4
# #    /   \
# #   7     2
# #  / \   / \
# # 9   6 3   1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            self.trim(root)
            return root
        else:
            return None

    def trim(self, node):
        if node.left is not None and node.right is not None:
            self.trim(node.left)
            self.trim(node.right)
            node.left, node.right = node.right, node.left
        elif node.left is not None:
            self.trim(node.left)
            node.right = node.left
            node.left = None
        elif node.right is not None:
            self.trim(node.right)
            node.left = node.right
            node.right = None