class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
def find_item(root, item):

    if root == None :
        return False
    if root.data == item:
        return  True
    elif find_item(root.left, item):
        return  True
    elif find_item(root.right, item):
        return True
    else :
        return  False
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(9)

    print(find_item(root, 00))