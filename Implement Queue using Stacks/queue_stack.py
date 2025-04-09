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


class MyQueue(object):
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stack.push(x)

    def pop(self):
        """
        :rtype: int
        """
        self._transfer()
        return self.out_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self._transfer()
        return self.out_stack.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def _transfer(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())