from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        merged = []

        nums.sort(key=lambda x: x[0])

        # makes merge between overlap paths
        for num in nums:
            if not merged or merged[-1][1] < num[0]:
                merged.append(num)
            else:
                merged[-1][1] = max(merged[-1][1], num[1])

        qtd = 0

        # counts the range of each path then sum
        for path in merged:
            qtd += path[1] - path[0] + 1

        return qtd


print(Solution().numberOfPoints(nums=[[3, 6], [1, 5], [4, 7]]))
