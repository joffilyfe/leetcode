# https://leetcode.com/problems/sort-array-by-parity/description/


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        even_index = 0
        odd_index = len(nums) - 1

        # def comparator(item1, item2):
        #     if item1 % 2 == 0:
        #         return -1
        #     elif item2 % 2 == 0:
        #         return 1
        #     else:
        #         return 0

        # nums.sort(key=cmp_to_key(comparator))

        for n in nums:
            if n % 2 == 0:
                result[even_index] = n
                even_index += 1
            else:
                result[odd_index] = n
                odd_index -= 1

        return result
