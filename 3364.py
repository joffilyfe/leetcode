import unittest
from typing import List


class SolutionOn2:
    """This is the naive approach:

    I)   First find every single possible sub array using a nested loop.
    II)  Sum the sub array items
    III) Check if the sub array size matches the l and r conditions
    IV)  Check if the Sum is greater than 0 and less than previous min and save it
    """
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        right = 0
        left = 0
        size = len(nums) + 1
        res = 1001 * 1001  # the maximum value if we sum all the elements from the list
        totalSum = 0

        for i in range(size):
            for j in range(i + 1, size):
                totalSum = sum(nums[i:j])

                windowSize = j - i

                if totalSum > 0 and windowSize >= l and windowSize <= r:
                    res = min(res, totalSum)

        if res == 1001 * 1001:
            return -1

        return res


class Solution:
    """ This is the optimised solution running on O(N)

    I)  First we define the window size l and r
    II) Then we do the sum for that specific window size
    III) Then from the window_size til the last Index of the array
    IV) Update the total sum with the current sum (minus the element outsite the limit (current - size) == left - 1) + current number
    """
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = 100 * 1001

        # try each possible window size from l to r
        for window_size in range(l, r + 1):
            current_sum = sum(nums[:window_size])

            # check first window
            if current_sum > 0:
                min_sum = min(min_sum, current_sum)

            # slide the window
            for i in range(window_size, n):
                # remove leftmost element, add rightmost element
                # this is the trick, we remove the element that not fit in the window and add the new one
                current_sum = current_sum - nums[i - window_size] + nums[i]

                if current_sum > 0:
                    min_sum = min(min_sum, current_sum)

        return min_sum if min_sum != 100 * 1001 else -1



class Tests(unittest.TestCase):
    def test_one(self):
        nums = [3, -2, 1, 4]
        l = 2
        r = 3

        self.assertEqual(Solution().minimumSumSubarray(nums, l, r), 1)

    def test_two(self):
        nums = [-2, 2, -3, 1]
        l = 2
        r = 3

        self.assertEqual(Solution().minimumSumSubarray(nums, l, r), -1)

    def test_three(self):
        nums = [17, 13]
        l = 1
        r = 2

        self.assertEqual(Solution().minimumSumSubarray(nums, l, r), 13)

    def test_four(self):
        nums = [5,8,-6]
        l = 1
        r = 3

        self.assertEqual(Solution().minimumSumSubarray(nums, l, r), 2)


    def test_five(self):
        nums = [-23,2,-12]
        l = 1
        r = 2
        self.assertEqual(Solution().minimumSumSubarray(nums, l, r), 2)



if __name__ == "__main__":
    unittest.main()



# 2
# nums = [5,8,-6]
# l = 1
# r = 3

# 12
# nums = [-1,23,12]
# l = 1
# r = 1

# 2
