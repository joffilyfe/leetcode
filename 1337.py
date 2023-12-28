from typing import List, Tuple
import heapq
import unittest


def number_of_targets(row: List[int]) -> int:
    """Using binary seach we find what is the lefiest index where number 1 is.
    For this specific problem we are targetting the last index of number 1."""

    left = 0
    right = len(row) - 1

    while left <= right:
        middle = (left + right) // 2

        if row[middle] == 1:
            left = middle + 1
        else:
            right = middle - 1

    return left


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Using heap we create a priority qeue based in the number of ones for each row. More ones least the priority"""

        heap: List[Tuple[int, int]] = []

        for i, row in enumerate(mat):
            heapq.heappush(heap, (number_of_targets(row), i))

        return [heapq.heappop(heap)[1] for _ in range(k)]


class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(
            Solution().kWeakestRows(
                mat=[
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1],
                ],
                k=3,
            ),
            [2, 0, 3],
        )

    def test_second(self):
        self.assertEqual(
            Solution().kWeakestRows(
                mat=[[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], k=2
            ),
            [0, 2],
        )


if __name__ == "__main__":
    unittest.main()
