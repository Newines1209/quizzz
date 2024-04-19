class LinearQueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def display(self):
        print(self.stack1 + self.stack2)

q_stack = LinearQueueUsingStack()
q_stack.enqueue(1)
q_stack.enqueue(2)
q_stack.enqueue(3)
q_stack.display()
q_stack.dequeue()
q_stack.display()
