from typing import List
import unittest

class Solution:
  def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
    i, j, k = 0, 1, 2
    size = len(nums) - 1
    count = 0

    while i <= size and j <= size and k <= size:
        if nums[k] - nums[j] > diff:
            j += 1
        elif nums[k] - nums[j] < diff:
            k += 1
        else:
            if nums[j] - nums[i] > diff:
                i += 1
            elif nums[j] - nums[i] < diff:
                j += 1
            else:
                count += 1
                j += 1
                i += 1

    return count


class Test(unittest.TestCase):
    @unittest.skip(reason='just skip')
    def test_first(self):
        self.assertEqual(Solution().arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3), 2)

    @unittest.skip(reason='just skip')
    def test_second(self):
        self.assertEqual(Solution().arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2), 2)

    def test_third(self):
        self.assertEqual(Solution().arithmeticTriplets(nums = [0,1,2], diff = 0), 1)

unittest.main()
