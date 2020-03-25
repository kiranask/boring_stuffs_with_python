class DoublyLinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

a.next = b
b.next = c

b.prev = a
c.prev = b

print(a.value)
print(b.value)
print(c.value)

print(c.prev.value)
print(b.prev.next.value)

