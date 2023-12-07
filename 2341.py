# https://leetcode.com/problems/maximum-number-of-pairs-in-array/
"""
You are given a 0-indexed integer array nums. In one operation, you may do the following:

Choose two integers in nums that are equal.
Remove both integers from nums, forming a pair.
The operation is done on nums as many times as possible.

Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.



Example 1:

Input: nums = [1,3,2,1,3,2,2]
Output: [3,1]
Explanation:
Form a pair with nums[0] and nums[3] and remove them from nums. Now, nums = [3,2,3,2,2].
Form a pair with nums[0] and nums[2] and remove them from nums. Now, nums = [2,2,2].
Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [2].
No more pairs can be formed. A total of 3 pairs have been formed, and there is 1 number leftover in nums.
Example 2:

Input: nums = [1,1]
Output: [1,0]
Explanation: Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [].
No more pairs can be formed. A total of 1 pair has been formed, and there are 0 numbers leftover in nums.
Example 3:

Input: nums = [0]
Output: [0,1]
Explanation: No pairs can be formed, and there is 1 number leftover in nums.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        table = {}

        for num in nums:
            if table.get(num) is None:
                table[num] = 1
            else:
                table[num] += 1

        pairs = 0
        leftover = 0

        for qtd in table.values():
            pair = qtd // 2

            if qtd % 2 == 0:
                pairs += pair
            else:
                leftover += 1
                pairs += pair

        return [pairs, leftover]


import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(Solution().numberOfPairs(nums=[1, 3, 2, 1, 3, 2, 2]), [3, 1])


if __name__ == "__main__":
    unittest.main()
