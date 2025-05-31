import unittest
from typing import List

class SolutionNaive:
    """This is my naive solution where I move left and right pointers,
    summing the current item and removing the leftmost when right - left == k
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, 0
        n = len(nums) - 1
        avg = float('-inf')
        totalSum = 0.0

        if n == 1:
            return nums[-1]

        while right <= n:
            if right - left == k:
                avg = max(avg, totalSum / k)

                totalSum -= nums[left]

                left += 1
            else:
                totalSum += nums[right]
                right += 1

        avg = max(avg, totalSum / k)

        return avg


class Solution:
    """This is the optimal solution where we rely only in the window size

    I)   Initialise the sum from 0 to k
    II)  Then loop from k to the last index of num
    III) update the window sum: current sum + actual - leftmost (while window slides)
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)

        return max_sum / k


class Tests(unittest.TestCase):
    def test_one(self):
        nums = [1,12,-5,-6,50,3]
        k = 4

        self.assertEqual(Solution().findMaxAverage(nums, k), 12.75)

    def test_two(self):
        nums = [-1]
        k = 1

        self.assertEqual(Solution().findMaxAverage(nums, k), -1)

    def test_three(self):
        nums = [0,1,1,3,3]
        k = 4

        self.assertEqual(Solution().findMaxAverage(nums, k), 2.0)


if __name__ == "__main__":
    unittest.main()
