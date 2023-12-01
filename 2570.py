from typing import List
from collections import defaultdict


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        qtd = defaultdict(lambda: 0)
        values = defaultdict(lambda: 0)

        for num in nums1:
            qtd[num[0]] += 1
            values[num[0]] += num[1]

        for num in nums2:
            qtd[num[0]] += 1
            values[num[0]] += num[1]

        ordered = [list(n) for n in sorted(values.items(), key=lambda x: x[0])]

        return ordered


print(
    Solution().mergeArrays(
        nums1=[[1, 2], [2, 3], [4, 5]], nums2=[[1, 4], [3, 2], [4, 1]]
    )
)
