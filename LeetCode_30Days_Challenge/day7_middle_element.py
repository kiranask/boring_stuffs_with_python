"""
Given a non-empty, singly linked list with head node head,
return a middle node of linked list.
If there are two middle nodes, return the second middle node.

"""


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

class Solution():

    def middleNode(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)


# How to Link these nodes together
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None
solution = Solution()
print(solution.middleNode(a))