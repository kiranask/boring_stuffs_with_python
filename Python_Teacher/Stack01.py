class Stack:
    def __init__(self):
        self.stack = []

    # Push element onto stack
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    # Pop element from stack
    def pop(self):
        if self.is_empty():
            return "Stack Underflow! Cannot pop."
        return self.stack.pop()

    # Peek top element
    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        return self.stack[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Get stack size
    def size(self):
        return len(self.stack)


# --------------------------
# Demo usage
if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push("Raj")

    print("Current Stack:", s.stack)
    print("Top element:", s.peek())
    print("Popped element:", s.pop())
    print("Stack after pop:", s.stack)
    print("Is empty?", s.is_empty())
    print("Size of stack:", s.size())
