from typing import List
import unittest


class Solution:
    # O(nlog(n)) approach where we sort the array to find the two biggest values
    # def maxProduct(self, nums: List[int]) -> int:
    #     nums.sort()
    #     return (nums[-2] - 1) * (nums[-1] - 1)

    # O(n) approach where we iterate over the list to find what are the two biggest values
    def maxProduct(self, nums: List[int]) -> int:
        num1 = 0
        num2 = 0

        for n in nums:
            if n > num1:
                num2 = num1
                num1 = n
            else:
                num2 = max(n, num2)

        return (num1 - 1) * (num2 - 1)


class Test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().maxProduct(nums=[3, 4, 5, 2]), 12)

    def test_second(self):
        self.assertEqual(Solution().maxProduct(nums=[1, 5, 4, 5]), 16)

    def test_third(self):
        self.assertEqual(Solution().maxProduct(nums=[10, 11]), 90)


if __name__ == "__main__":
    unittest.main()
