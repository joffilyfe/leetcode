# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

"""
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.



Example 1:

Input: nums = [1,2,3,3]
Output: 3
Example 2:

Input: nums = [2,1,2,5,3,2]
Output: 2
Example 3:

Input: nums = [5,1,5,2,5,3,5,4]
Output: 5


Constraints:

2 <= n <= 5000
nums.length == 2 * n
0 <= nums[i] <= 104
nums contains n + 1 unique elements and one of them is repeated exactly n times.
"""

from typing import List
import unittest

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        table: dict[int, int] = {}

        for num in nums:
            if table.get(num) is None:
                table[num] = 1
            else:
                table[num] += 1

        size = len(nums)

        result = 0

        for key, qtd in table.items():
            if qtd == size // 2:
                result = key
                break

        return result


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(Solution().repeatedNTimes(nums=[2, 1, 2, 5, 3, 2]), 2)


if __name__ == "__main__":
    unittest.main()
