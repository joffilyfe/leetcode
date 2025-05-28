from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next}"


class Solution:
    """My initial naive Solution

    With this solution I'm always going to the end then linking it to the head
    then breaking the previous link with the last which makes the prev node to be the last one.
    """

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        current = head
        i = 0
        size = 0

        while current:
            current = current.next
            size += 1

        current = head

        while i < (k % size):
            while current.next and current.next.next:
                current = current.next

            prev = current
            last = current.next

            last.next = head
            prev.next = None
            head = last

            i += 1
            current = head

        return head


class Solution2:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        current = head
        size = 1

        while current.next:
            current = current.next
            size += 1

        last = current
        last.next = head  # here the last is linked with the first one

        # now we need to interate over the list to count where we're going to break the link
        # then the next before breaking gonna be the head

        i = 0
        current = head

        # the number of operation is equal to how many nodes we want to bring from
        # back to the init. K can be pretty big. We can get the module of k per the size
        # of the list than we have the maximum nodes we can bring to front.frozenset
        operations = (k % size)
        until = size - operations - 1

        # When we have the number of operations we need to think backwards,
        # from the last node to the head how many are going to be bring forward?
        # Then we can just get the size - number of operations - 1 (0-index-list)
        # then we find in what node we should break the .next and set the head
        while current and i < until:
            current = current.next
            i += 1


        head = current.next
        current.next = None

        return head


head = None
current = None
# nums = [1, 2, 3, 4, 5]
nums = [1, 2]
k = 1

for i, val in enumerate(reversed(nums)):
    node = ListNode(val=val, next=current)

    if i == len(nums) - 1:
        head = node

    current = node


print(f"LinkedList: {head}")

head = Solution2().rotateRight(head=head, k=k)

print(f"LinkedList: {head}")
