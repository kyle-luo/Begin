# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is not None:
            output = []
            depth = 0
            def trav(node, depth):
                depth += 1
                if len(output) < depth:
                    output.append([])
                output[depth - 1].append(node.val)
                if node.left is not None:
                    trav(node.left, depth)
                if node.right is not None:
                    trav(node.right, depth)
            trav(root, depth)
            return [sum(x)/len(x) for x in output]
        else:
            return []


class Solution2:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is not None:
            nodes = [root]
            output = []
            while nodes != []:
                s = 0
                new_nodes = []
                for node in nodes:
                    s += node.val
                    if node.left is not None:
                        new_nodes.append(node.left)
                    if node.right is not None:
                        new_nodes.append(node.right)
                output.append(s / len(nodes))
                nodes = new_nodes
            return output
        else:
            return []