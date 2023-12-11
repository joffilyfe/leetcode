# https://leetcode.com/problems/neither-minimum-nor-maximum/description/


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) <= 2:
            return -1

        return nums[len(nums) // 2]
