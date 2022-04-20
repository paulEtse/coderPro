import unittest

from _10_04_2022.linked_list import ListNode, Solution


class Test_Solution(unittest.TestCase):
    def test_linked_list(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        self.assertEqual(l1.value_from_node(), 342)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        self.assertEqual(l2.value_from_node(), 465)

        self.assertEqual(str(Solution().addTwoNumbers(l1, l2)), "708")
