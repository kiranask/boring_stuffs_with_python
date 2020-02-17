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
print(c.next.data)




# def check_circle(node):
#     slow = node
#     fast = node
#     print("check")
#     while fast.next != None and fast != None:
#         slow = node.next
#         fast = node.next.next
#         if slow == fast:
#             return True

print(check_circle(a))

