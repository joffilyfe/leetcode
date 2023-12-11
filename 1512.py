# https://leetcode.com/problems/number-of-good-pairs/
# 1512. Number of Good Pairs
"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

from typing import List
from collections import defaultdict


class Solution:
    # this is a O(n ^ 2 ) solution because we're interating twice over the list
    # def numIdenticalPairs(self, nums: List[int]) -> int:
    #   qtd = 0

    #   for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #       if nums[i] == nums[j]:
    #         qtd += 1

    #   return qtd

    # this is a O(n) solutin where we count how
    # many entries a number has in the array then we can apply
    # this formula https://www.reddit.com/r/mathematics/comments/v3tgpx/dont_understand_why_n_n_1_2/
    # to find out how many pairs it has
    def numIdenticalPairs(self, nums: List[int]) -> int:
        table: dict[int, int] = defaultdict(lambda: 0)
        count = 0

        for number in nums:
            table[number] += 1

        for value in table.values():
            if value < 1:
                continue

            count += value * (value - 1) // 2

        return count


import unittest


class Test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]), 4)

    def test_second(self):
        self.assertEqual(Solution().numIdenticalPairs(nums=[1, 1, 1, 1]), 6)

    def test_third(self):
        self.assertEqual(Solution().numIdenticalPairs(nums=[1, 2, 3]), 0)


if __name__ == "__main__":
    unittest.main()
