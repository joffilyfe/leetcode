import unittest
from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxList = deque()
        minList = deque()
        n = len(nums)
        max_length = 0
        left = 0

        for right in range(n):
            num = nums[right]

            # The idea is to keep two lists with max and min values at X point of the array
            # when my number is greater than the number in the deque then we pop it until it's
            # not true anymore
            while maxList and num > maxList[-1]:
                maxList.pop()

            # To track the min we do the same, pop until my number is lesser than the last
            # of the deque.
            while minList and num < minList[-1]:
                minList.pop()

            # then I append it (in the end or it will be bigger or there are a bigger number at index 0)
            maxList.append(num)

            # The same for minList
            minList.append(num)

            # So, while the condition given by the problem is broken by our max & min lists
            # we loop and remove the bigger and the min number from the deque
            # then increase the left pointer
            while maxList and minList and abs(maxList[0] - minList[0]) > limit:
                if maxList[0] == nums[left]:
                    maxList.popleft()
                if minList[0] == nums[left]:
                    minList.popleft()

                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


class Tests(unittest.TestCase):
    def test_one(self):
        nums = [8, 2, 4, 7]
        limit = 4

        self.assertEqual(Solution().longestSubarray(nums, limit), 2)


if __name__ == "__main__":
    unittest.main()
