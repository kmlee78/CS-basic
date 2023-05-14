class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None

    def pop(self):
        if len(self.stack) != 0:
            item = self.stack.pop()
            return item
        else:
            return None
