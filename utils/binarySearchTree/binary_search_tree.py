class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def preorder(self):
        res = self.value
        if self.left:
            res += self.left.preorder()
        if self.right:
            res += self.right.preorder()
        return res
