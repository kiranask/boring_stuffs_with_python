def check_circle(node):
    slow = node
    fast = node
    print("check")
    while fast.next != None and fast != None:
        slow = node.next
        fast = node.next.next
        if slow == fast:
            return True

print(check_circle(a))
