from operator import xor
from typing import Optional
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return res


class Tests(unittest.TestCase):

    def fetch_list(self, head: Optional[ListNode]):
        values = []
        while head:
            values.append(head.val)

            head = head.next

        return values

    def test_one(self):
        head = ListNode(1, next=ListNode(1, next=ListNode(2)))
        values = self.fetch_list(Solution().deleteDuplicates(head=head))

        self.assertEqual(values, [1, 2])

    def test_two(self):
        head = ListNode(1, next=ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(3)))))
        values = self.fetch_list(Solution().deleteDuplicates(head=head))

        self.assertEqual(values, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
