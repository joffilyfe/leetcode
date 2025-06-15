from typing import List


class Solution:
    """The intuition behind this problem is to use the monotonic stack approach.

    We're looking for the "next greater" but instead replacing we are calculating the distance between
    them.

    We store the index in the stack to make it easier to find what is the distance between the numbers.
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        result = [0] * size
        stack = []

        for i in range(size):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index

            stack.append(i)

        return result
