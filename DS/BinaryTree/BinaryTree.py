# simple binary tree
# in this implementation, a node is inserted between an existing node and the root
class BinaryTree():
    def __init__(self,root):
      self.left = None
      self.right = None
      self.root = root

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.root = value
    def getNodeValue(self):
        return self.root

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree
