# A binary tree is univalued if every node in the tree has the same value.
#
# Return true if and only if the given tree is univalued.
#
#
# Example 1:
#
# Input: [1,1,1,1,1,null,1]
# Output: true
#
# Example 2:
#
# Input: [2,2,2,5,2]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        self.key = root.val
        self.result = True
        self._checkVal(root)
        return self.result

    def _checkVal(self, node):
        if node.val != self.key:
            self.result = False
            return
        if node.left is not None: self._checkVal(node.left)
        if node.right is not None: self._checkVal(node.right)


class Solution2:
    def isUnivalTree(self, root: TreeNode) -> bool:
        key = root.val
        search = [root]
        while search != []:
            cur = search.pop()
            if cur.val != key:
                return False
            if cur.left is not None:
                search.append(cur.left)
            if cur.right is not None:
                search.append(cur.right)
        return True