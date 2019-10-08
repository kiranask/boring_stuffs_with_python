class Queue:
    def __init__(self):
        self.que = []
    def enqueue(self,item):
        self.que.insert(0,item)
    def dequeue(self):
        return self.que.pop()
    def isEmpty(self):
        return self.que == []
    def size(self):
        return len(self.que)

    def peek(self):
        return self.que[-1]
q= Queue()
q.enqueue(10)
q.enqueue(20)

print(q.peek())
print(q.dequeue())
print(q.peek())