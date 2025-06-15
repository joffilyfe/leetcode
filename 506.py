import heapq
import unittest
from typing import List

class Solution:
    """This is a typical K largest elements. We need to use a Max Heap approach.

    The score basically sets the result position. After building the hea
    we pop elements until it finishes.

    When building the heap we store items indexes in order to be able
    to set their result accordinely in the right place.
    """
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        size = len(score)
        results = [""] * size

        for i in range(size):
            v = score[i]
            heapq.heappush(heap, (-v, i))


        i = 0
        while len(heap) > 0:
            v, index = heapq.heappop(heap)
            value = i + 1


            if i == 0:
                value = "Gold Medal"
            elif i == 1:
                value = "Silver Medal"
            elif i == 2:
                value = "Bronze Medal"

            results[index] = str(value)

            i += 1

        return results


class Tests(unittest.TestCase):
    def test_one(self):
        score = [5,4,3,2,1]
        expected = ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

        self.assertEqual(Solution().findRelativeRanks(score), expected)

if __name__ == "__main__":
    unittest.main()
