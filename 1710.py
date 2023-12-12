from typing import List
import unittest

# https://leetcode.com/problems/maximum-units-on-a-truck/


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        count = 0

        boxTypes.sort(key=lambda box: box[1], reverse=True)

        for types in boxTypes:
            boxes = types[0]
            amount = types[1]

            if truckSize - boxes >= 0:
                count += boxes * amount
                truckSize -= boxes
            else:
                boxes = boxes - abs(truckSize - boxes)
                count += boxes * amount
                truckSize -= boxes

        return count


class Test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(
            Solution().maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4), 8
        )

    def test_second(self):
        self.assertEqual(
            Solution().maximumUnits(
                boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10
            ),
            91,
        )


if __name__ == "__main__":
    unittest.main()
