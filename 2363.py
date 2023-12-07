from typing import List


class Solution:
    def mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]]
    ) -> List[List[int]]:
        table = {}

        for item in items1:
            if table.get(item[0]) is None:
                table[item[0]] = item[1]
            else:
                table[item[0]] += item[1]

        for item in items2:
            if table.get(item[0]) is None:
                table[item[0]] = item[1]
            else:
                table[item[0]] += item[1]

        return [[key, table[key]] for key in sorted(table.keys())]


import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(
            Solution().mergeSimilarItems(
                items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]]
            ),
            [[1, 6], [3, 9], [4, 5]],
        )


if __name__ == "__main__":
    unittest.main()
