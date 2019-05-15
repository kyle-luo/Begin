# Given an n-ary tree, return the postorder traversal of its nodes' values.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.output = []
        if root is None:
            return self.output
        else:
            self._traversal(root, self.output)
            return self.output

    def _traversal(self, node, output):
        if node.children:
            for child in node.children:
                self._traversal(child, output)
            output.append(node.val)
        else:
            output.append(node.val)