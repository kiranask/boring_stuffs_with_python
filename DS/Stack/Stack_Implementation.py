
class Stack():

    def __init__(self):
        self.stack = []



# It increases size by 1
    def push(self, item):
        self.stack.append(item)


# Function to remove an item from Stack.
# It decreases size by 1
    def pop(self):
        return self.stack.pop()

    def peek(self ):
        return self.stack[len(self.stack)-1]
# Function to determine the size of the Stack
    def size(self, stack):
        return len(self.stack)


# Stack is empty if the size is 0
    def isEmpty(self, stack):
        return self.stack == []

    # Function to add an item to Stack .

stack_new = Stack()
stack_new.push(10)
stack_new.push(20)
stack_new.push(30)

print(stack_new.pop())