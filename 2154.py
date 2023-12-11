from typing import List
import unittest
from collections import defaultdict

# https://leetcode.com/problems/keep-multiplying-found-values-by-two/


class Solution:
    def _search(self, array: List[int], value: int) -> bool:
        left = 0
        right = len(array) - 1

        while left <= right:
            middle = (left + right) // 2

            if array[middle] == value:
                return True
            elif value > array[middle]:
                left = middle + 1
            elif value < array[middle]:
                right = middle - 1

        return False

    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = list(sorted(nums))

        while self._search(nums, original):
            original *= 2

        return original


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(
            self.solution.findFinalValue(nums=[5, 3, 6, 1, 12], original=3), 24
        )

    def test_second(self):
        self.assertEqual(self.solution.findFinalValue(nums=[2, 7, 9], original=4), 4)


if __name__ == '__main__':
    unittest.main()
