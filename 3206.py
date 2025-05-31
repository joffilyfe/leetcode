from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res = 0
        n = len(colors)

        for i in range(n):
            if colors[i] == 0 and colors[(i + 1) % n] == 1 and colors[(i + 2) % n] == 0:
                res += 1
            elif colors[i] == 1 and colors[(i + 1) % n] == 0 and colors[(i + 2) % n] == 1:
                res += 1

        return res


colors = [0, 1, 0, 1]
res = Solution().numberOfAlternatingGroups(colors)
print(res)
