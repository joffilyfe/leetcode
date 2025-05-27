# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List
import unittest


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n**2 for n in nums])


class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        The ideia behind this algorithm is to create a answer array with the same
        size of the nums.

        The asn array will be populated from right to left.

        While interating the nums array we check what number is greater then we populated in the N position
        on the ans list then reduce 1 from the N tracker.

        if the left is greater then we move the I pointer forward, otherwise we move J backwards.
        """

        i = 0
        j = len(nums) - 1
        n = j
        asn = [0] * len(nums)

        while i <= j:
            left = pow(nums[i], 2)
            right = pow(nums[j], 2)

            if left > right:
                asn[n] = left
                i += 1
            else:
                asn[n] = right
                j -= 1

            n -= 1

        return asn


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
