from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        table = {}

        for number in nums:
            if table.get(number) is None:
                table[number] = 1
            else:
                table[number] += 1

        size = len(nums) // 2

        qtd = 0

        for value in table.values():
            qtd += value // 2

        return size == qtd


print(Solution().divideArray(nums=[1, 2, 3, 4]))
