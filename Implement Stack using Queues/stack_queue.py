class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def add(self, item):
        self.items.append(item) 
    def pop(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        return self.items.pop(0)
    def peek(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        return self.items[0]
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return "Queue: [" + ", ".join(str(item) for item in self.items) + "]"


class MyStack(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.add(x)
        while self.q1:
            self.q2.add(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.pop()

    def top(self):
        return self.q1.peek()

    def empty(self):
        return not self.q1

