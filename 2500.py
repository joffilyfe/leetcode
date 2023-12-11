from typing import List
import unittest


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        count = 0

        for i in range(len(grid)):
            grid[i] = list(sorted(grid[i]))

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        i = len(grid)
        j = len(grid[0]) - 1

        while j >= 0:
            greatest = 0

            for r in range(i):
                if grid[r][j] > greatest:
                    greatest = grid[r][j]

            count += greatest
            j -= 1

        return count


class Test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().deleteGreatestValue(grid=[[1, 2, 4], [3, 3, 1]]), 8)

    def test_second(self):
        self.assertEqual(Solution().deleteGreatestValue(grid=[[10]]), 10)

    def test_third(self):
        self.assertEqual(Solution().deleteGreatestValue(grid=[[10, 1, 2]]), 13)

    def test_fourth(self):
        self.assertEqual(Solution().deleteGreatestValue(grid=[[1, 2, 3], [1, 3, 5]]), 9)


if __name__ == '__main__':
    unittest.main()
