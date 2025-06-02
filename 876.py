from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head


        # The idea here is that if the fast moves always 2 times faster
        # then when it reaches the end of the list
        # the slow point will be at the middle
        while fast and slow and fast.next:
            slow = slow.next
            fast = fast.next.next

        # consequently we can return the slow node
        return slow
