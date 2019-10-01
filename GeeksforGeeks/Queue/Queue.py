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
q= Queue()
q.enqueue(10)
q.enqueue(20)

for items in range(q.size()):
    print(q.dequeue())