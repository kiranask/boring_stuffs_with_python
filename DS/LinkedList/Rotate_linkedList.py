"""

1 > 2 > 3 > 4 > 5 > 6

pivot element is 4

5 > 6 > 1 > 2 > 3 > 4

How to solve:

1. take 2 pointer P and Q

2. P should travel till Pivot
3. Q should travel till end of the list.

4. Q should point to head.
5. P should point now null because it is the end of the new linked list.
6. Next to Pivot should become the First element, self.head

"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_node(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def append(self,data):
        new_node = Node(data)
        current = self.head
        if current is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def rotate(self,n):
        p = self.head
        q = self.head
        #1 > 2 > 3 > 4 > 5 > 6
        prev = self.head
        count = 0
        while p and count < n:
            p = prev
            p = p.next
            count +=1
        p = prev
        # p.data = pivot
        while q :
            prev = q
            q = q.next
        q = prev
        print(q.data)
        # q.data last element
        q.next = self.head
        self.head = p.next

        p.next = None 






llist = LinkedList()
llist.append('1')
llist.append('2')
llist.append('3')
llist.append('4')
llist.append('5')
llist.append('6')
llist.rotate(4)
