# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example, given a 3-ary tree:
#
# We should return its level order traversal:
#
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        self.dic = {}
        self.max_deep = 0
        output = []
        if root is not None:
            self.dic[0] = [root.val]
            self.trav(root.children, 0)
            for x in range(self.max_deep):
                output.append(self.dic[x])
        return output

    def trav(self, node, deep):
        deep += 1
        self.dic[deep] = self.dic.get(deep, [])
        if deep > self.max_deep:
            self.max_deep = deep
        for x in node:
            self.dic[deep].append(x.val)
            if x.children is not None:
                self.trav(x.children, deep)


class Solution2:
    def levelOrder(self, root) -> List[List[int]]:
        output = []
        if root is not None:
            output.append([root.val])
            self.trav(root.children, 0, output)
            output.pop()
        return output

    def trav(self, node, deep, output):
        deep += 1
        if (len(output) - 1 < deep): output.append([])
        for x in node:
            output[deep].append(x.val)
            if x.children is not None:
                self.trav(x.children, deep, output)