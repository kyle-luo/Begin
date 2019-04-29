class Node:

    def __init__(self, item = None):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = Node()

    def append(self, item):
        new_node = Node(item)
        pre = self.head
        while pre.next != None:
            pre = pre.next
        pre.next = new_node

    def show(self):
        show = []
        pre = self.head
        while pre.next != None:
            pre = pre.next
            show.append(pre.item)
        print(show)
        return None

    def length(self):
        count = 0
        pre = self.head
        while pre.next != None:
            count += 1
            pre = pre.next
        return count

    def generate(self, items):
        for x in items:
            LinkedList.append(self, x)

    def get(self, index):
        pre = self.head
        for x in range(index):
            pre = pre.next
        return pre.item


ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.show()
ll.length()
ll.get(1)
#
#
# aa = LinkedList()
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# aa.generate(list)
# aa.show()
