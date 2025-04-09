from collections import defaultdict

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

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


class FreqStack(object):

    def __init__(self):
        self.stack = Stack()
        self.control = Queue()
        self.frequencies = defaultdict()


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.push(val)
        self.frequencies[val] += 1

    def pop(self):
        """
        :rtype: int
        """
        if self.stack.is_empty():
            return None
        max_freq = max(self.frequencies.values())
        while not self.stack.is_empty():
            self.control.add(self.stack.pop())
        v = Queue()
        while not self.control.is_empty():
            value = self.control.pop()
            if not (self.frequencies[value] == max_freq):
                self.stack.push(value)
            else:
                v.add(value)
        return v.pop()
        
        