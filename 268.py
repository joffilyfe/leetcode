from typing import List
import unittest


class OptimalSolution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        totalSum = sum(nums)
        expectedSum = ((size + 1) * size) // 2

        return expectedSum - totalSum

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)

        for i in range(size):
            if i != nums[i]:
                return i

        return size
        # left = 0
        # right = len(nums) - 1

        # while left <= right:
        #     middle = left + (right - left) // 2

        #     if nums[middle] == middle:
        #         left = middle + 1
        #     else:
        #         right = middle - 1


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @unittest.skip("")
    def test_zero(self):
        self.assertEqual(self.solution.missingNumber(nums=[0]), 1)

    @unittest.skip("")
    def test_first(self):
        self.assertEqual(self.solution.missingNumber(nums=[3, 0, 1]), 2)

    def test_second(self):
        self.assertEqual(self.solution.missingNumber(nums=[0, 1]), 2)

    def test_third(self):
        self.assertEqual(
            self.solution.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]), 8
        )

    def test_fourth(self):
        self.assertEqual(self.solution.missingNumber(nums=[0, 2, 3]), 1)

    def test_fifth(self):
        self.assertEqual(
            self.solution.missingNumber(nums=[1, 8, 4, 6, 2, 0, 9, 7, 5]), 3
        )


if __name__ == "__main__":
    unittest.main()
