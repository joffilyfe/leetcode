from typing import List

class Solution:
    # O(n ^ 2)
    # O(n)
    def countKDifference(self, nums: List[int], k: int) -> int:
        table = {}
        result = 0

        for i in range(len(nums)):
            if table.get(nums[i] - k):
                result += table.get(nums[i] - k)

            if table.get(nums[i] + k):
                result += table.get(nums[i] + k)

            if table.get(nums[i]) is  None:
                table[nums[i]] = 1
            else:
                table[nums[i]] += 1

        return result




print(Solution().countKDifference(nums=[1,2,2,1], k=1))
