from typing import List
import unittest


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            sum = numbers[i] + numbers[j]

            if sum == target:
                return [i + 1, j + 1]
            elif sum > target:
                j -= 1
            elif sum < target:
                i += 1

        return [-1, -1]


class Tests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(Solution().twoSum(numbers=[2, 7, 11, 15], target=9), [1, 2])

    def test_two(self):
        self.assertEqual(Solution().twoSum(numbers=[2, 3, 4], target=6), [1, 3])

    def test_three(self):
        self.assertEqual(Solution().twoSum(numbers=[-1, 0], target=-1), [1, 2])


if __name__ == "__main__":
    unittest.main()
