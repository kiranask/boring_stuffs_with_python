class BinaryTree:
    def __init__(self,root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            # Push the existing left child sub tree downwards.
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setRootVal(self,root):
        self.key = root
    def getRootVal(self):
        return self.key


r = BinaryTree("a")
print(r.getRootVal())
r.insertLeft("b")
print(r.getLeftChild().getRootVal())
