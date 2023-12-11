from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # for each item in the PRICE LIST
        # check if there is a discount
        # the discount is calculated as:
        # given position price[i] >= price[j]
        # then d = price[i] - price[j] if price[j] < price[i]
        # otherwise d = price[i]

        size = len(prices)
        monotonic_stack = []
        result = [0] * size

        # for i in range(size - 1, -1, -1):
        for i in range(size - 1, -1, -1):
            current = prices[i]

            while len(monotonic_stack) > 0 and monotonic_stack[-1] > current:
                monotonic_stack.pop()

            if not monotonic_stack:
                result[i] = current
            else:
                result[i] = current - monotonic_stack[-1]

            monotonic_stack.append(current)

        return result


import unittest


class Test(unittest.TestCase):
    def test_first_case(self):
        self.assertEqual(
            Solution().finalPrices(prices=[8, 4, 6, 2, 3]), [4, 2, 4, 2, 3]
        )


if __name__ == '__main__':
    unittest.main()
