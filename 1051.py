# https://leetcode.com/problems/height-checker/description/

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = list(sorted(heights))

        count = 0

        for i in range(len(expected)):
            if expected[i] != heights[i]:
                count += 1

        return count
