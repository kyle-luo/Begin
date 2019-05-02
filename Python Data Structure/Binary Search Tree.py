class node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("value is already in the BST.")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
        else:
            print("BST is not built yet.")

    def _print_tree(self, cur_node):
        if cur_node.left is not None:
            print(cur_node.value)
            self._print_tree(cur_node.left)
        elif cur_node.right is not None:
            print(cur_node.value)
            self._print_tree(cur_node.right)
        else:
            print(cur_node.value)

    def search(self, value):
        if value != self.root.value:
            self._search(value, self.root)
        else:
            return True

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value:
            self._search(value, cur_node.left)
        elif value > cur_node.value:
            self._search(value, cur_node.right)
        else:
            return False

new = BST()
new.insert(1)
new.insert(2)
new.insert(3)
new.insert(4)
new.insert(5)

new.print_tree()

print(new.search(1))
print(new.search(3))
print(new.search(5))
