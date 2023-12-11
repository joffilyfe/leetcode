from functools import cmp_to_key
from typing import List
import unittest


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        def sort(item):
            return item[k]

        return sorted(score, key=sort, reverse=True)


class Test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(
            Solution().sortTheStudents(
                score=[[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], k=2
            ),
            [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]],
        )

    def test_first(self):
        self.assertEqual(
            Solution().sortTheStudents(score=[[3, 4], [5, 6]], k=0), [[5, 6], [3, 4]]
        )


if __name__ == '__main__':
    unittest.main()
