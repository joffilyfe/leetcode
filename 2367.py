from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        qtd = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        # print("{} - {} = 3".format(nums[j],  nums[i]))
                        # print("{} - {} = 3".format(nums[k],  nums[j]))
                        qtd += 1
        print(qtd)


Solution().arithmeticTriplets(nums=[4, 5, 6, 7, 8, 9], diff=2)
