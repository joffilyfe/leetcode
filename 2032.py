from typing import List
import unittest
from collections import defaultdict


class Solution:

    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        table: dict[int, int] = defaultdict(lambda: 0)

        for n in set(nums1):
            table[n] += 1

        for n in set(nums2):
            table[n] += 1

        for n in set(nums3):
            table[n] += 1

        return sorted([n for n, v in table.items() if v > 1])


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(
            self.solution.twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]),
            sorted([3, 2]),
        )

    def test_second(self):
        self.assertEqual(
            self.solution.twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]),
            sorted([2, 3, 1]),
        )


if __name__ == '__main__':
    unittest.main()
