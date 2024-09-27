class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)

# How to Link these nodes together
a.next = b
b.next = c
# c.next = a

print(a.data)
print(b.data)
print(c.data)





def check_circle(head):
    slow = head
    fast = head

    while fast.next != None and fast != None:
        slow = head.next
        fast = head.next.next
        # if slow == fast:
        #     return True
        # else:
        #     return False
    return slow.data
print(check_circle(a))

