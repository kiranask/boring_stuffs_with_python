# Python3 program to find maximum
# and minimum in a Bianry Tree

# A class to create a new node
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Returns maximum value in a
# given Binary Tree

max_data = float('-infinity')
def findMax(root):
    # Base case

    global  max_data
    if (root == None):
        return max_data

    # Return maximum of 3 values:
    # 1) Root's data 2) Max in Left Subtree
    # 3) Max in right subtree
    res = root.data
    if res > max_data :
        max_data =res
    findMax(root.left)
    findMax(root.right)

    return max_data

# Driver Code
if __name__ == '__main__':
    root = newNode(2)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(6)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(11)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)

    print("Maximum element is",
          findMax(root))

# This code is contributed by PranchalK
