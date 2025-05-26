import unittest
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        element = nums[0]

        for el in nums:
            if i == 0 or i == 1 or nums[i-2] != el:
                nums[i] = el
                i += 1

        return i



class Tests(unittest.TestCase):

    def test_one(self):
        nums = [1,1,1,2,2,3]
        expected = [1,1,2,2,3]

        k = Solution().removeDuplicates(nums=nums)

        for i in range(k):
            assert nums[i] == expected[i]


    def test_two(self):
        nums = [0,0,1,1,1,1,2,3,3]
        expected = [0,0,1,1,2,3,3]

        k = Solution().removeDuplicates(nums=nums)

        for i in range(k):
            assert nums[i] == expected[i]


if __name__ == '__main__':
    unittest.main()
