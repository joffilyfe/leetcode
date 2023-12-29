from typing import List
import unittest


def binary_search_negatives(nums, size):
    right = size - 1
    left = 0

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] > 0:
            right -= 1
        elif nums[middle] < 0:
            left += 1
        else:
            right -= 1

    return left


def binary_search_positives(nums, left, size):
    right = size - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] <= 0:
            left += 1
        elif nums[middle] > 0:
            right -= 1

    return size - left


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        size = len(nums)
        negatives = binary_search_negatives(nums, size)
        positives = binary_search_positives(nums, negatives, size)

        return max(negatives, positives)


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(self.solution.maximumCount(nums=[-2, -1, -1, 1, 2, 3]), 3)

    def test_second(self):
        self.assertEqual(self.solution.maximumCount(nums=[5, 20, 66, 1314]), 4)

    def test_third(self):
        self.assertEqual(self.solution.maximumCount(nums=[-3, -2, -1, 0, 0, 1, 2]), 3)

    def test_fourth(self):
        nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.solution.maximumCount(nums), 0)

    def test_fifth(self):
        nums = [-2, -1, -1, 0, 0, 0]
        self.assertEqual(self.solution.maximumCount(nums), 3)


if __name__ == "__main__":
    unittest.main()
