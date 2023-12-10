# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/

from functools import cmp_to_key


def comparator(item1, item2):
    if item1[1] > item2[1]:
        return 1
    elif item1[1] < item2[1]:
        return -1
    else:
        if item1[0] > item2[0]:
            return 1
        else:
            return -1


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bin_count = []

        for n in arr:
            number_of_ones = 0

            while n > 0:
                n = n & (n - 1)
                number_of_ones += 1

            bin_count.append(number_of_ones)

        result = list(zip(arr, bin_count))
        result.sort(key=cmp_to_key(comparator))

        return [n for n, _ in result]
