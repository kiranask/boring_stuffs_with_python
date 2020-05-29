def reverse_linkedlist(head):
    previous = None
    current = head
    next_node  = None
# You know only current
    while current:
        next_node = current.next
        current.next = previous
        previous  = current
        current = next_node
    return previous

# Draw P <- C <- N




