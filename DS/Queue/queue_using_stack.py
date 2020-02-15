# Python3 program to implement Queue using
# two stacks with costly enQueue()

class QueueUsing2Stacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enQueue(self, element):
        self.in_stack.append(element)
    def deQueue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # Put all the elements of in_stack to out_stack and pop
        return self.out_stack.pop()

if __name__ == '__main__':
    q = QueueUsing2Stacks()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(8)
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())

