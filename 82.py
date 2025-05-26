import unittest
from typing import Optional

# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fake = ListNode(-1, next=head)
        current, prev = head, fake

        while current:
            while current.next and current.val == current.next.val:
                current = current.next

            if prev and prev.next == current:
                prev = prev.next
                current = current.next
            elif prev:
                prev.next = current.next
                current = prev.next

        return fake.next


class Tests(unittest.TestCase):

    def fetch_list(self, head: Optional[ListNode]):
        values = []
        while head:
            values.append(head.val)

            head = head.next

        return values

    def test_one(self):
        # [1,2,3,3,4,4,5]
        head = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(3, next=ListNode(4, next=ListNode(4, ListNode(5)))))))
        values = self.fetch_list(Solution().deleteDuplicates(head=head))

        self.assertEqual(values, [1, 2, 5])

    def test_two(self):
        # [1,1,1,2,3]

        head = ListNode(1, next=ListNode(1, next=ListNode(1, next=ListNode(2, next=ListNode(3)))))
        values = self.fetch_list(Solution().deleteDuplicates(head=head))

        self.assertEqual(values, [2, 3])


if __name__ == '__main__':
    unittest.main()
