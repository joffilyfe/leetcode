from typing import List
import unittest

class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:

    #     # brute force approach
    #     for i, n in enumerate(nums):
    #         if n == target:
    #             return i

    #         if n > target:
    #             return i


    #     return len(nums)

    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1

            while left <= right:
                middle = (left + right) // 2


                if target == nums[middle]:
                    return middle
                elif target > nums[middle]:
                    left = middle + 1
                elif target < nums[middle]:
                    right = middle - 1

            return left

        index = binary_search(nums=nums, target=target)

        return index

class Test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().searchInsert(nums = [1,3,5,6], target = 5), 2)

    def test_second(self):
        self.assertEqual(Solution().searchInsert(nums = [1,3,5,6], target = 2), 1)

    def test_third(self):
        self.assertEqual(Solution().searchInsert(nums = [1,3,5,6], target = 7), 4)


if __name__ == '__main__':
    unittest.main()

