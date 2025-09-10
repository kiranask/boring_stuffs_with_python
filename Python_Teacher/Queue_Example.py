class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue → add element at rear
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    # Dequeue → remove element from front
    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow! Cannot dequeue."
        return self.queue.pop(0)

    # Peek → front element
    def front(self):
        if self.is_empty():
            return "Queue is empty."
        return self.queue[0]

    # Check if empty
    def is_empty(self):
        return len(self.queue) == 0

    # Get size
    def size(self):
        return len(self.queue)


# --------------------------
# Demo usage
if __name__ == "__main__":
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print("Current Queue:", q.queue)
    print("Front element:", q.front())
    print("Dequeued element:", q.dequeue())
    print("Queue after dequeue:", q.queue)
    print("Is empty?", q.is_empty())
    print("Size of queue:", q.size())
