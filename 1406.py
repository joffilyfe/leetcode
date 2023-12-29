# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

from typing import List
import unittest


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        total = sum(nums)
        total_result = 0
        result: List[int] = []

        for n in nums:
            result.append(n)
            total -= n
            total_result += n

            if total_result > total:
                return result

        return result


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(self.solution.minSubsequence(nums=[4, 3, 10, 9, 8]), [10, 9])

    def test_second(self):
        self.assertEqual(self.solution.minSubsequence(nums=[4, 4, 7, 6, 7]), [7, 7, 6])


if __name__ == "__main__":
    unittest.main()
