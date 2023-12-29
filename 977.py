# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List
import unittest


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n**2 for n in nums])


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(
            self.solution.sortedSquares(nums=[-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100]
        )

    def test_second(self):
        self.assertEqual(
            self.solution.sortedSquares(nums=[-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121]
        )


if __name__ == "__main__":
    unittest.main()
