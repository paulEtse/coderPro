class Stack:
    def __init__(self):
        self.table = []

    def push(self, value):
        self.table.append(value)

    def empty(self):
        return len(self.table) == 0

    def top(self):
        return self.table[-1]

    def pop(self):
        return self.table.pop()
