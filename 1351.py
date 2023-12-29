from typing import List
import unittest


def binary_search_for_the_first_negative_number(nums: List[int], size: int) -> int:
    left = 0
    right = size - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] > 0 or nums[middle] == 0:
            left += 1
        elif nums[middle] < 0:
            right -= 1

    return size - left


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        size = len(grid[0])

        for row in grid:
            count += binary_search_for_the_first_negative_number(row, size)

        return count


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(
            self.solution.countNegatives(
                grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
            ),
            8,
        )

    def test_second(self):
        self.assertEqual(
            self.solution.countNegatives(grid=[[3, 2], [1, 0]]),
            0,
        )

    def test_third(self):
        self.assertEqual(
            self.solution.countNegatives(grid=[[1, -1], [-1, -1]]),
            3,
        )


if __name__ == "__main__":
    unittest.main()
