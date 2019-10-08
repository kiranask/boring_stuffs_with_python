# https://medium.com/@codingfreak/binary-tree-interview-questions-and-practice-problems-439df7e5ea1f
class Queue:
    def __init__(self):
        self.que = []
    def enqueue(self,item):
        self.que.insert(0,item)
    def dequeue(self):
        return self.que.pop()
    def isEmpty(self):
        return self.que == []
    def size(self):
        return len(self.que)
    def peek(self):
        return self.que[-1].value


class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return  self.pre_order_print(tree.root, "")
        elif traversal_type == 'inorder':
            return  self.in_order_print(tree.root, "")
        elif traversal_type == 'postorder':
            return self.post_order_print(tree.root, "")

        elif traversal_type == 'levelorder':
            return self.level_order_traversal(tree.root)
        else :
            return  False


    def pre_order_print(self, start, traversal):
    # Root - left - Right
        if start:
            traversal += (str(start.value) + " - ")
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal

    def in_order_print(self, start, traversal):
    # Left - Root - Right
        if start :
            traversal = self.in_order_print(start.left, traversal)
            traversal += (str(start.value) + " - ")
            traversal = self.in_order_print(start.right, traversal)
        return  traversal

    def post_order_print(self, start, traversal):
    # Left - Right _ Root
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal = self.in_order_print(start.right, traversal)
            traversal += (str(start.value) + " - ")
        return traversal

    def level_order_traversal(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ''
        while queue.size() > 0:
            traversal += str(queue.peek())
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return  traversal




tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
tree.root.right.left = Node(7)
print(tree.print_tree("levelorder"))




