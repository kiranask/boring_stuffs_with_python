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
# add at the end is called append.
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        # Find out the last node to add append.
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

# add at the beginning is called
    def prepend(self,data):
        new_node = Node(data)
        #make current self.head as next node.
        new_node.next = self.head
        #make new node as self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        # If prev_node does not exist, then return
        if not prev_node:
            print('Previous Node is not present')
            return
        #make new node pointing to next of pre_node.
        new_node = Node(data)
        #make pre_node pointing new_mode
        new_node.next = prev_node.next
        prev_node.next = new_node
    def delete_a_node(self,key):
        #if the first node is key
        cur_node = self.head
        if cur_node and cur_node.data == key :
            self.head = cur_node.next
            cur_node = None
            return
        #check the key is present or not.
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

        # Go to the position.
        while count != pos and cur_node:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return "Index out of range"
        #Make prev_node as current node.
        prev_node.next =  cur_node.next
        cur_node = None

llist = LinkedList()
llist.append('A')

# llist.prepend('E')
# llist.insert_after_node(llist.head, 'X')
#llist.delete_a_node('E')
# llist.delete_node_at_pos(1)
llist.print_list()