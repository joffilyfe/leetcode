"""
There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9.

You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where:

The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.

Return the number of rods that have all three colors of rings on them.

Input: rings = "B0B6G0R6R0R6G9"
Output: 1
Explanation:
- The rod labeled 0 holds 3 rings with all colors: red, green, and blue.
- The rod labeled 6 holds 3 rings, but it only has red and blue.
- The rod labeled 9 holds only a green ring.
Thus, the number of rods with all three colors is 1.
"""

class Solution:
    # O(n)
    def countPoints(self, rings: str) -> int:
        rods = {}
        qtd = 0

        for i in range(0, len(rings) - 1, 2):
            color = rings[i]
            rod = rings[i + 1]

            if rods.get(rod) is None:
                rods[rod] = set(color)
            else:
                rods[rod].add(color)

        for colors in rods.values():
            if len(colors) == 3:
                qtd += 1

        return qtd




print(Solution().countPoints(rings='G4'))
