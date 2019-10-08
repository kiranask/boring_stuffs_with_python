# Python3 program to implement Queue using
# two stacks with costly enQueue()

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):

        # Move all elements from s1 to s2
        while len(self.s1) != 0:

            top =self.s1.pop()
            self.s2.append(top)

        # Push item into self.s1
        self.s1.append(x)

        # Push everything back from s2 to s1
        while len(self.s2) != 0:

            top =self.s2.pop()
            self.s1.append(top)

        # Dequeue an item from the queue

    def deQueue(self):

        # if first Stack is empty
        if len(self.s1) == 0:
            print("Q is Empty")

        # Return top of self.s1
        return self.s1.pop()

    # Driver code


if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(8)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())

# This code is contributed by PranchalK
