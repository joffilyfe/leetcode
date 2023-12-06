from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        table = {}

        for n in nums:
            if table.get(n) is None:
                table[n] = 1
            else:
                table[n] += 1

        qtd = 0

        for key, value in table.items():
            if value == 1:
                qtd += key

        return qtd


print(Solution().sumOfUnique(nums = [1,2,3,2]))
