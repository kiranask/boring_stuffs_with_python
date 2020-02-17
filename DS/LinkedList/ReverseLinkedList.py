def reverse_linkedlist(head):
    previous = None
    current = head
    next_node  = None

    while current:
        next_node = current.next
        current.next = previous
        previous  = current
        current = next_node
    return previous




