# Given a n-ary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        else:
            return self._depth(root)

    def _depth(self, node):
        depth = 0
        if node.children is not None:
            for child in node.children:
                newd = self._depth(child)
                if newd > depth:
                    depth = newd
        return depth + 1


