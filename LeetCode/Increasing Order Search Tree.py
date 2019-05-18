# Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return []
        else:
            self.output = []
            self._order(root)
            cur_node = TreeNode(None)
            n_tree = cur_node
            for i in range(len(self.output)):
                cur_node.right = TreeNode(self.output[i])
                cur_node = cur_node.right
            return n_tree.right

    def _order(self, node):
        if node.left is not None:
            self._order(node.left)
        self.output.append(node.val)
        if node.right is not None:
            self._order(node.right)