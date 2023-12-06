# Hashtable
# 1 two sum
# address: https://leetcode.com/problems/two-sum/

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


from typing import List

class Solution:

  # this is O(n ^ 2) because we do two loops over the list
  # def twoSum(self, nums: List[int], target: int) -> List[int]:
  #   for i in range(0, len(nums)):
  #     for j in range(i + 1, len(nums)):
  #       if nums[i] + nums[j] == target:
  #         return [i, j]

  # this is O(n) because we iterate only once over the list
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    table = {}

    for i in range(0, len(nums)):
      complement = target - nums[i]

      if table.get(complement) is not None:
        return [table.get(complement), i]

      table[nums[i]] = i

