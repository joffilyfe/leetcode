from typing import List
import unittest


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        size = len(nums)

        for i in range(size - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            z = size - 1

            while j < z:
                sum = nums[i] + nums[j] + nums[z]

                if sum > 0:
                    z -= 1
                elif sum < 0:
                    j += 1
                else:
                    triplets.append([nums[i], nums[j], nums[z]])
                    j += 1
                    z -= 1

                    while nums[j] == nums[j - 1] and j < z:
                        j += 1

        return triplets


class Tests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(
            Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]]
        )

    def test_two(self):
        self.assertEqual(Solution().threeSum(nums=[0, 0, 1]), [])

    def test_three(self):
        self.assertEqual(Solution().threeSum(nums=[0, 0, 0]), [[0, 0, 0]])


if __name__ == "__main__":
    unittest.main()
