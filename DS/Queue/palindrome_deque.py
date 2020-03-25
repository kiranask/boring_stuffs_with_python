from pythonds import Deque

def palindrome_checker(string_to_check):
    queue = Deque()
    for ch in string_to_check:
        queue.addFront(ch)
    stillEqual = True
    while queue.size()>1 and stillEqual :
        first = queue.removeFront()
        last = queue.removeRear()

        if first != last :
            stillEqual = False

    return stillEqual


print(palindrome_checker('12321'))