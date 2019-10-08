class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
min_data = float('infinity')
def find_min_tree(root):
    global min_data
    if root == None:
        return min_data

    res = root.data
    if res < min_data:
        min_data = res
    find_min_tree(root.left)
    find_min_tree(root.right)
    return  min_data

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(9)

    print(find_min_tree(root))