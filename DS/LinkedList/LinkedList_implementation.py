class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous Node is not present')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def delete_a_node(self,key):
        cur_node = self.head
        if cur_node and cur_node.data == key :
            self.head = cur_node.next
            cur_node = None
            return
        prev_node = None
        while cur_node.data != key :
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return "Given Node Not Found"
        # cur_node which we are planning to delete
        prev_node.next  = cur_node.next
        cur_node = None
    def delete_node_at_pos(self, pos):
        cur_node = self.head
        if pos == 0 :
            self.head = cur_node.next
            cur_node = None
            return
        prev_node = None
        count = 1
        while count != pos and cur_node:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return "Index out of range"

        prev_node.next =  cur_node.next
        cur_node = None

llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
# llist.prepend('E')
# llist.insert_after_node(llist.head, 'X')
#llist.delete_a_node('E')
llist.delete_node_at_pos(1)
llist.print_list()