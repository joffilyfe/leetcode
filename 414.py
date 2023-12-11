from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = 0
        second = 0
        third = 0

        nums = list(sorted(set(nums)))
        # for num in nums:
        #     if num > first:
        #         first = num
        #     elif num > second:
        #         second = num
        #     elif num > third:
        #         third = num

        # return third or second or first
        if len(nums) <= 2:
            return nums[-1]

        return nums[-3]


import unittest


class Tests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(Solution().thirdMax(nums=[2, 2, 3, 1]), 1)

    def test_two(self):
        self.assertEqual(Solution().thirdMax(nums=[3, 2, 1]), 1)

    def test_three(self):
        self.assertEqual(Solution().thirdMax(nums=[1, 2, 0]), 0)


if __name__ == '__main__':
    unittest.main()
