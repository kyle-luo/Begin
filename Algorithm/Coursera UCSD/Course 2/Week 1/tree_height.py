# python3

import sys
import threading


class Node:
    def __init__(self, val=None):
        self.val = val
        self.child = []


class Tree:
    def __init__(self, nodes_num):
        self.root = None
        self.nodes = [Node() for _ in range(nodes_num)]

    def insert(self, val, parent):
        if parent == -1:
            self.nodes[val].val = val
            self.root = self.nodes[val]
        else:
            self.nodes[val].val = val
            self.nodes[parent].child.append(self.nodes[val])

    def check_depth(self):
        if self.root is not None:
            return self._check_depth(self.root)

    def _check_depth(self, node):
        if len(node.child) == 0:
            return 1
        depths = [self._check_depth(c) for c in node.child]
        return max(depths) + 1


def compute_height(n, parents):
    # Replace this code with a faster implementation
    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    # return max_height
    tree = Tree(n)
    for i in range(n):
        tree.insert(i, parents[i])
    return tree.check_depth()


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()


# print(compute_height(5, [4, -1, 4, 1, 1]))
