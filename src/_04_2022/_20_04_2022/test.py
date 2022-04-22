import unittest

from src._04_2022._20_04_2022.find_ceiling_floor import findCeilingFloor
from utils.binarySearchTree.binary_search_tree import Node


class TestSolution(unittest.TestCase):
    def test_find_ceiling_floor(self):
        root = Node(8)
        root.left = Node(4)
        root.right = Node(12)

        root.left.left = Node(2)
        root.left.right = Node(6)

        root.right.left = Node(10)
        root.right.right = Node(14)

        self.assertEqual(findCeilingFloor(root, 5), (4, 6))

        self.assertEqual(findCeilingFloor(root, 11), (10, 12))

        self.assertEqual(findCeilingFloor(root, 1), (None, 2))

        self.assertEqual(findCeilingFloor(root, 6), (6, 6))

        self.assertEqual(findCeilingFloor(root, 15), (14, None))
