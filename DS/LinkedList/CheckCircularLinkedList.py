def check_circle(node):
    slow = node
    fast = node
    print("check")
    is_circular = False
    while fast.next != None and fast != None and is_circular :
        slow = node.next
        fast = node.next.next
        if slow == fast:
            return True
print(check_circle(node))
