from typing import List
import unittest
import itertools
import bisect


class Solution:
    # def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
    #     result: List[int] = []
    #     numsSize = len(nums)

    #     for query in queries:
    #         total, i = 0, 0
    #         while i < numsSize and (total + nums[i] <= query):
    #             total += nums[i]
    #             i += 1

    #         result.append(i)

    #     return result

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """Prefix sum approach: it uses itertools.accumulate to create a new
        list with the result of accumulation of previous + current item.

        Than it uses bisect.bisect_right to find the next index of greater number of n.
        """
        nums.sort()
        numsSum = list(itertools.accumulate(nums))
        return [bisect.bisect_right(numsSum, n) for n in queries]


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(
            self.solution.answerQueries(nums=[1, 2, 4, 5], queries=[3, 10, 21]),
            [2, 3, 4],
        )

    def test_second(self):
        self.assertEqual(
            self.solution.answerQueries(nums=[2, 3, 4, 5], queries=[1]),
            [0],
        )


if __name__ == "__main__":
    unittest.main()
