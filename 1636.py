from typing import List
import unittest

from functools import cmp_to_key


def comparator(item1, item2):
    if item1[1] > item2[1]:
        return 1
    elif item1[1] < item2[1]:
        return -1
    else:
        if item1[0] > item2[0]:
            return -1
        else:
            return 1


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        table: dict[int, int] = {}

        for n in nums:
            table[n] = table.get(n, 0) + 1

        result = list(table.items())
        result.sort(key=cmp_to_key(comparator))
        result = [[n] * v for n, v in result]

        return [item for row in result for item in row]


class Test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(
            Solution().frequencySort(nums=[1, 1, 2, 2, 2, 3]), [3, 1, 1, 2, 2, 2]
        )

    def test_second(self):
        self.assertEqual(
            Solution().frequencySort(nums=[2, 3, 1, 3, 2]), [1, 3, 3, 2, 2]
        )

    def test_third(self):
        self.assertEqual(Solution().frequencySort(nums=[1, 5, 0, 5]), [1, 0, 5, 5])


if __name__ == '__main__':
    unittest.main()
