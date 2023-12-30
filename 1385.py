from copy import copy
from typing import List
import unittest


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        size = len(arr2) - 1
        count = len(arr1)

        for number in arr1:
            left = 0
            right = size

            while left <= right:
                middle = (left + right) // 2
                if abs(arr2[middle] - number) <= d:
                    count -= 1
                    break
                elif number < arr2[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

        return count


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(
            self.solution.findTheDistanceValue(arr1=[4, 5, 8], arr2=[1, 8, 9, 10], d=2),
            2,
        )

    def test_second(self):
        self.assertEqual(
            self.solution.findTheDistanceValue(
                arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3
            ),
            2,
        )


if __name__ == "__main__":
    unittest.main()
