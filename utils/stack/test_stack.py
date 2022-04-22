import unittest

from utils.stack.stack import Stack


class TestSTack(unittest.TestCase):
    def test_top(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        stack.pop()
        self.assertEqual(stack.pop(), 1)

    def test_empty(self):
        stack = Stack()
        self.assertTrue(stack.empty())
        stack.push(2)
        self.assertFalse(stack.empty())
        stack.pop()
        self.assertTrue(stack.empty())

    def test_push_pop(self):
        stack = Stack()
        stack.push(2)
        self.assertEqual(stack.pop(), 2)


if __name__ == "__main__":
    unittest.main()
