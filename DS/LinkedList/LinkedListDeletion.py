class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def delete(self,key):
        if key is None:
            return
        cur_node = self.head
        if key == cur_node.data:
            self.head = cur_node.next
            cur_node = None
            return
        pre_node = None
        while key != cur_node.data:
            pre_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        pre_node.next = cur_node.next
        cur_node = None
