from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for i in range(0, len(nums) - 1, 2):
            count += nums[i]

        return count


print(Solution().arrayPairSum(nums=[6, 2, 6, 5, 1, 2]))
