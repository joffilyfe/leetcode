from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        size = len(code)
        res = [0] * size

        if k == 0:
            return res

        # This is the brute force solution
        # for i in range(size):
        #     if k > 0:
        #         for j in range(i + 1, i + k + 1):
        #             res[i] += code[j % size]
        #     else:
        #         for j in range(i - abs(k), i):
        #             res[i] += code[(j + size) % size]
        left = 1
        right = k

        if k < 0:
            left = size - abs(k)
            right = size - 1

        # we need the initial sum that will be set for the first
        # element in the array
        windowSum = sum(code[left:right + 1])

        for i in range(size):
            res[i] = windowSum # here
            # Then we remove the first element from the sum:
            # The first element from the sum is at index 1! We dont include [0]
            # in the sum.
            windowSum -= code[left % size]
            # Then we update the Sum with the next right element
            windowSum += code[(right + 1) % size]

            left += 1
            right += 1

        return res


# [0,0,0,0]
code = [1, 2, 3, 4]
k = 0

# [12, 5, 6, 13]
code = [2, 4, 9, 3]
k = -2

# # [12, 10, 16, 13]
# code = [5, 7, 1, 4]
# k = 3

print(Solution().decrypt(code, k))
