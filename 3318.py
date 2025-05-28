from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        numbers = {}
        size = len(nums) - k + 1
        answer = [-1] * size
        j = 0

        for i, number in enumerate(nums):
            numbers[number] = numbers.get(number, 0) + 1

            # building while iterating over the list
            # in every loop we need to check if the window is full (k)
            # when the window is full then we extract the first x-sum:
            #
            # filter the numbers that have value (ocurrencies) > x
            # if occurencies are equal then keep only the higher key
            # then sum result of previous operation
            # then add to the res array

            if i - k + 1 >= 0:
                # this is the logic required by the problem. We need to get the top
                # elements sorted by the qty then if they draw the bigger number will
                # be selected
                sums = sorted([(v, key) for key, v in numbers.items()], reverse=True)
                # then keep only the X top elements
                answer[j] = sum([pair[0] * pair[1] for pair in sums[:x]])
                j += 1

                # need to reduce the quantity of the number i - k + 1 positions ago
                numbers[nums[i - k + 1]] -= 1

        return answer

nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2

nums = [3,8,7,8,7,5]
k = 2
x = 2

print(Solution().findXSum(nums, k, x))
