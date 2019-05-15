# Given an n-ary tree, return the preorder traversal of its nodes' values.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        if root is not None:
            self._traversal(root, output)
        return output

    def _traversal(self, node, list):
        list.append(node.val)
        if node.children is not None:
            for child in node.children:
                self._traversal(child, list)