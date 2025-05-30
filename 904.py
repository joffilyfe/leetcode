import unittest
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        table = {}

        left = 0
        right = 0
        res = 0
        size = len(fruits)

        while right < size:
            current_fruit = fruits[right]
            oldest_fruid = fruits[left]

            table[current_fruit] = table.get(current_fruit, 0) + 1

            if len(table.keys()) > 2:
                table[oldest_fruid] -= 1

                if table[oldest_fruid] == 0:
                    del table[oldest_fruid]

                left += 1

            right += 1

            res = max(res, right - left)

        return res


class Tests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(Solution().totalFruit(fruits=[1, 2, 1]), 3)

    def test_two(self):
        self.assertEqual(
            Solution().totalFruit(fruits=[5, 9, 0, 9, 6, 9, 6, 9, 9, 9]), 7
        )


if __name__ == "__main__":
    unittest.main()
