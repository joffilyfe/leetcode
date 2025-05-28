from typing import List

# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    """
    This a easy question that we can use sliding window approach to solve it.

    The SW solution requires a size for that window (this question sets K) where
    the we need to check the data within the boundaries.

    In this question we need to find two numbes athat are equal and j > i and
    the |j - i| <= k. This last bit is important because is where we should
    understand the window size.

    So, the numbers set is the window that we add data into [1, 2, 3] (this is a window of 3 elements),
    then we iterate over the list, check if the number is already into the set, if so it's done. Otherwise,
    add the number into the window of work, then check if the window is larger than K, if so remove windows' "first"
    element.
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numbers = set()

        for i in range(len(nums)):
            if nums[i] in numbers:
                return True

            numbers.add(nums[i])

            if len(numbers) > k:
                numbers.remove(nums[i - k])

        return False
