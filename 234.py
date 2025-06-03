from typing import Optional
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """The intuiton of this problem is very simple:
        Create a new array and store the linked list data there
        use two pointer technique to find if the chars are the same from left and right moving at the same time.


    However, the problem states we cannot use additional store size to do it. How can we solve?

    We can split the linked list in the middle then revert the second half and compare it with the
    list initing in the head.

    1) Use flow and fast pointers
    2) When fast hit Null then slow is in the middle
    3) Revert the second half of LL (prev = None, current = slow).
    4) After reverting the `prev` will have the HEAD of the second half (reverted)
    5) Loop throught the nodes checking their values
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        left = head
        right = prev

        while left and right:
            if right.val != left.val:
                return False

            left = left.next
            right = right.next

        return True


class Tests(unittest.TestCase):
    def test_one(self):
        prev = ListNode()
        head = prev

        for v in [1, 2, 2, 1]:
            n = ListNode(val=v)
            prev.next = n
            prev = n


        self.assertEqual(Solution().isPalindrome(head.next), True)


    def test_two(self):
        prev = ListNode()
        head = prev

        for v in [1, 2, 3, 1]:
            n = ListNode(val=v)
            prev.next = n
            prev = n


        self.assertEqual(Solution().isPalindrome(head.next), False)


    def test_three(self):
        prev = ListNode()
        head = prev

        for v in [0, 2, 1]:
            n = ListNode(val=v)
            prev.next = n
            prev = n


        self.assertEqual(Solution().isPalindrome(head.next), False)


if __name__ == "__main__":
    unittest.main()
