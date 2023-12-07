# https://leetcode.com/problems/build-array-from-permutation/description/

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [0] * size

        for i in range(size):
            result[i] = nums[nums[i]]

        return result
