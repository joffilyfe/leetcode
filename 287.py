# https://leetcode.com/problems/find-the-duplicate-number/

import unittest
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        memory = {}

        for n in nums:
            if memory.get(n):
                return n

            memory[n] = True

        return -1



class Tests(unittest.TestCase):

    def test_one(self):
        nums = [1,3,4,2,2]

        assert Solution().findDuplicate(nums=nums) == 2


    def test_two(self):
        nums = [3,1,3,4,2]

        assert Solution().findDuplicate(nums=nums) == 3


if __name__ == '__main__':
    unittest.main()
