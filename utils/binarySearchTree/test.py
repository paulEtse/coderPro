import unittest

from utils.binarySearchTree.binary_search_tree import Node


class TestSolution(unittest.TestCase):
    def test_binary_tree(self):
        root = Node("a")
        root.left = Node("b")
        root.right = Node("c")
        root.left.left = Node("d")
        root.left.right = Node("e")
        root.right.left = Node("f")

        self.assertEqual(root.preorder(), "abdecf")
