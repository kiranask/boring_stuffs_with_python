from pythonds.basic import Stack
stack = Stack()
def reverse_string(string):
    for char in string:
        # print(char)
        stack.push(char)
    reverse = ''
    while not stack.isEmpty():
        reverse += stack.pop()
    return reverse
print(reverse_string("123456789"))