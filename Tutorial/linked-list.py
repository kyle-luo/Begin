class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def trav(self):
        print(self.val)
        if self.next:
            self.next.trav()


head = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)

head.next = node1
node1.next = node2

print(head.next.next.val)

head.trav()

x = head
x = node1

# print(x.next)
# print(head.next)
#
# x = head
# x.next = node1
# x = node1
# print(head.next)