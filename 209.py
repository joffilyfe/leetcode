from typing import List

class Solution:
    """The intuition here is pretty simple.
    1) We need to find each sub array where the condition is match S >= target.
    2) Once the condition is found we calculate the minimum size of that sub array.
    3) Then we remove from the total sum the leftmost element and move left forwrd.
    4) Go to the next loop and do the same.
    5) End with the smallest number of elements that match the criteria
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # This is a O(N) time solution with O(1) space
        size = len(nums)
        left = 0
        totalSum = 0
        min_size = float("inf")


        for right in range(size):
            totalSum += nums[right]

            while totalSum >= target:
                min_size = min(min_size, right - left + 1)

                totalSum = totalSum - nums[left]
                left += 1

        return int(min_size) if min_size != float("inf") else 0
