from typing import List
import unittest
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        table = defaultdict(lambda: 0)

        for number in arr:
            table[number] += 1

        number_of_items = len(table.values())
        number_of_items_in_the_set = len(set(table.values()))

        return number_of_items == number_of_items_in_the_set


class Test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]), True)

    def test_second(self):
        self.assertEqual(Solution().uniqueOccurrences(arr=[1, 2]), False)

    def test_third(self):
        self.assertEqual(Solution().uniqueOccurrences(arr=[1, 2, 1]), True)


unittest.main()
