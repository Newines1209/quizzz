class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def enqueue(self, item):
        if len(self.queue) < self.capacity:
            self.queue.append(item)
        else:
            print("Queue is full")

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            print("Queue is empty")

    def display(self):
        print(self.queue)
q = LinearQueue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.dequeue()
q.display()
