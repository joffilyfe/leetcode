from typing import List
import unittest


# You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:

# 0 <= i < j < k < nums.length
# nums[i], nums[j], and nums[k] are pairwise distinct.
# In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
# Return the number of triplets that meet the conditions.


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        table = {}

        for n in nums:
            table[n] = table.get(n, 0) + 1

        count, prev, next = 0, 0, len(nums)

        for value in table.values():
            next -= value
            count += prev * value * next
            prev += value

        return count


class Test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().unequalTriplets(nums=[4, 4, 2, 4, 3]), 3)

    def test_second(self):
        self.assertEqual(Solution().unequalTriplets(nums=[1, 1, 1, 1, 1]), 0)

    def test_third(self):
        self.assertEqual(Solution().unequalTriplets(nums=[2, 1, 1, 1, 3]), 3)

    def test_forth(self):
        self.assertEqual(Solution().unequalTriplets(nums=[1, 2, 3, 4, 5, 6]), 20)


if __name__ == '__main__':
    unittest.main()
