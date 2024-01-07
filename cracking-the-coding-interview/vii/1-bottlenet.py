import unittest

# Example: Given an array of distinct integer values,
# count the number of pairs of integers that have difference k.
# For example, given the array {1, 7, 5, 9, 2, 12, 3} and
# the difference k = 2,there are four pairs with
# difference 2: (1, 3), (3, 5), (5, 7), (7, 9).

# the first approach is using brute force to iterate over the array nums
# from i to n and internally doing it from i + 1 to n
# until finding the last pair at (n, n).

# the O(n) approach is to dump the complement into as key into the
# hash table then iterate over the array again and try to find
# each num as key in the table. If it can be found then
# it has its pair.


class Solution:
    def finding_pairs_of_k(self, nums, k: int):
        table = {}
        count = 0

        for num in nums:
            table[num - k] = num

        for num in nums:
            if table.get(num, None):
                count += 1

        return count


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(
            self.solution.finding_pairs_of_k(nums=[1, 7, 5, 9, 2, 12, 3], k=2), 4
        )

    def test_second(self):
        self.assertEqual(
            self.solution.finding_pairs_of_k(nums=[1, 7, 5, 9, 2, 12, 3], k=10), 1
        )


if __name__ == "__main__":
    unittest.main()
