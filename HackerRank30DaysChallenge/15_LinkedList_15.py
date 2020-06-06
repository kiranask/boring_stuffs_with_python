class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        newNode = Node(data)
        """ is this the last node aka innermost node?"""
        if head == None:
            head = newNode
            return head
        else:
            """start at ottermost node """
            pointer = head
            """traverse the (data, next_node) pairs until next_node = None"""
            while pointer.next is not None:
                """there is an inner node, so increment to it"""
                pointer = pointer.next
            pointer.next = newNode
            """
            head was changed as we traversed the links, 
            so return it to calling method
            """
            return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head); 	  