# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

class Solution:
    def leafSimilar(self, root1, root2):
        list1 = []
        list2 = []
        self._leafs(root1, list1)
        self._leafs(root2, list2)
        return list1 == list2

    def _leafs(self, node, list):
        if node.left is not None:
            self._leafs(node.left, list)
        else:
            if node.right is None:
                list.append(node.val)
        if node.right is not None:
            self._leafs(node.right, list)
        else:
            if node.left is None:
                list.append(node.val)