from typing import List
import unittest
from collections import defaultdict


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        table = defaultdict(lambda: 0)

        for string in arr:
            table[string] += 1

        for string in arr:
            count += 1

            if table[string] > 1:
                count -= 1

            if count == k:
                return string

        return ""


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(
            self.solution.kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2), "a"
        )

    def test_second(self):
        self.assertEqual(self.solution.kthDistinct(arr=["aaa", "aa", "a"], k=1), "aaa")

    def test_third(self):
        self.assertEqual(self.solution.kthDistinct(arr=["a", "b", "a"], k=3), "")

    def test_fourth(self):
        self.assertEqual(self.solution.kthDistinct(arr=["a", "a", "b", "a"], k=1), "b")


unittest.main()
