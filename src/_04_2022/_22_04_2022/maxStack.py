from utils.stack.stack import Stack


class MaxStack:
    def __init__(self):
        self.memo = Stack()

    def push(self, val):
        if self.memo.empty():
            self.memo.push((val, val))
        else:
            self.memo.push((val, max(self.memo.top()[1], val)))

    def pop(self):
        self.memo.pop()

    def max(self):
        return self.memo.top()[1]
