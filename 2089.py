# https://leetcode.com/problems/find-target-indices-after-sorting-array
from typing import List
import unittest


def binary_search(nums, target):
    """Uses binary search to find the first target occurrence. After, iterates over the
    list until find all target occurrences."""

    left = 0
    right = len(nums) - 1
    total = right
    indexes = []

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == target:
            min = middle - 1
            max = middle

            while min >= 0 and nums[min] == target:
                indexes.append(min)
                min -= 1

            while max <= total and nums[max] == target:
                indexes.append(max)
                max += 1

            return indexes
        elif target < nums[middle]:
            right = middle - 1
        elif target > nums[middle]:
            left = middle + 1

    return indexes


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        return sorted(binary_search(nums, target))


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(
            self.solution.targetIndices(nums=[1, 2, 5, 2, 3], target=2), [1, 2]
        )

    def test_second(self):
        self.assertEqual(
            self.solution.targetIndices(nums=[100, 1, 100], target=100), [1, 2]
        )

    def test_third(self):
        self.assertEqual(
            self.solution.targetIndices(
                nums=[
                    11,
                    34,
                    78,
                    38,
                    8,
                    41,
                    97,
                    15,
                    16,
                    18,
                    97,
                    36,
                    21,
                    11,
                    85,
                    83,
                    36,
                    11,
                    45,
                    17,
                    93,
                    95,
                    70,
                    12,
                    16,
                    18,
                    13,
                    89,
                    97,
                    20,
                    86,
                    46,
                    24,
                    50,
                    45,
                    94,
                    89,
                    25,
                    61,
                    59,
                    51,
                    72,
                    74,
                    55,
                    4,
                    41,
                    47,
                    46,
                    45,
                    75,
                    93,
                    2,
                    61,
                    99,
                    39,
                    74,
                    49,
                    83,
                    53,
                    54,
                    22,
                    55,
                    89,
                    98,
                    48,
                    44,
                    87,
                    74,
                    25,
                ],
                target=45,
            ),
            [28, 29, 30],
        )

    def test_forth(self):
        self.assertEqual(
            self.solution.targetIndices(
                nums=[
                    33,
                    22,
                    49,
                    7,
                    2,
                    6,
                    13,
                    70,
                    59,
                    19,
                    21,
                    45,
                    98,
                    93,
                    32,
                    23,
                    89,
                    47,
                    17,
                    27,
                    11,
                    22,
                    93,
                    77,
                    52,
                    34,
                    75,
                    96,
                    48,
                    53,
                    44,
                    76,
                    76,
                    7,
                    48,
                    25,
                    68,
                    70,
                    48,
                    32,
                    89,
                    21,
                    12,
                    81,
                    65,
                    36,
                    92,
                    21,
                    94,
                    84,
                    77,
                    43,
                    4,
                    88,
                    78,
                    82,
                    94,
                    20,
                    52,
                    20,
                    16,
                    84,
                    83,
                    100,
                    84,
                    97,
                    49,
                    10,
                    12,
                    94,
                    88,
                    24,
                    1,
                    31,
                    81,
                    95,
                    92,
                    51,
                    36,
                    84,
                    48,
                    34,
                    85,
                    8,
                    3,
                    47,
                    46,
                    18,
                    84,
                    43,
                    42,
                    35,
                    97,
                    60,
                    93,
                    14,
                    92,
                    47,
                    44,
                    72,
                ],
                target=84,
            ),
            [75, 76, 77, 78, 79],
        )


if __name__ == "__main__":
    unittest.main()
