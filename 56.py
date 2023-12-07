# https://leetcode.com/problems/merge-intervals/description/

from typing import List
from operator import itemgetter


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


print(Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18], [23, 24]]))
# print(Solution().merge(intervals = [[1,4],[0,3]]))
# print(Solution().merge(intervals = [[1,4]]))
# print(Solution().merge(intervals = [[1,4],[5,6]]))
# print(Solution().merge(intervals = [[1,4],[2,3]]))
