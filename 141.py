from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head

        # The fast and slow approach move the fast pointer ahead the slow
        # so if there is a cycle the fast pointer will eventually find the slow pointer
        # that give us the confirmation of cycle into the list
        while slow and fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
