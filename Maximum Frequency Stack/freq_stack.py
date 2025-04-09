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

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.stack_freqs = defaultdict(Stack)
        self.max_freq = 0

    def push(self, val):
        self.freq[val] += 1
        if self.freq[val] > self.max_freq:
            self.max_freq = self.freq[val]
        self.stack_freqs[self.freq[val]].push(val)

    def pop(self):
        if self.max_freq == 0:
            return None
        val = self.stack_freqs[self.max_freq].pop()
        self.freq[val] -= 1
        if self.stack_freqs[self.max_freq].is_empty():
            self.max_freq -= 1
        return val