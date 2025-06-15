import heapq
from typing import List

class KthLargest:
    """The intuition behind this problem is to keep a min heap structure where
    after adding a new element we return the min element (at index 0).

    We need to keep the heap size equal to K so after adding we need to pop.
    """

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k

        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
