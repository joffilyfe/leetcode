# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/

class Solution:
    def minimumSum(self, num: int) -> int:
        ordered = sorted(str(num))

        return int(ordered[0] + ordered[2]) + int(ordered[1] + ordered[3])


import unittest


class Test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Solution().minimumSum(num=2932), 52)

    def test_second(self):
        self.assertEqual(Solution().minimumSum(num=4009), 13)


if __name__ == "__main__":
    unittest.main()
