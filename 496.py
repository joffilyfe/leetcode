from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        table = {}
        result = []

        for n in nums2:
            while len(stack) > 0 and n > stack[-1]:
                table[stack.pop()] = n

            stack.append(n)

        for n in nums1:
            if n in table:
                result.append(table[n])
            else:
                result.append(-1)

        return result


print(Solution().nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
