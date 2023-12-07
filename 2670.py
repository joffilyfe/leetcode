from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        qtd = len(nums)
        result = []

        for i in range(qtd):
            prefix = list(set(nums[0 : i + 1]))
            sufix = list(set(nums[i + 1 : qtd]))

            result.append(len(prefix) - len(sufix))

        return result


print(Solution().distinctDifferenceArray(nums=[1, 2, 3, 4, 5]))
