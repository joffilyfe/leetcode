# https://leetcode.com/problems/increasing-decreasing-string/description/

"""
You are given a string s. Reorder the string using the following algorithm:

1. Pick the smallest character from s and append it to the result.
2. Pick the smallest character from s which is greater than the last appended character to the result and append it.
3. Repeat step 2 until you cannot pick more characters.
4. Pick the largest character from s and append it to the result.
5. Pick the largest character from s which is smaller than the last appended character to the result and append it.
6. Repeat step 5 until you cannot pick more characters.
7. Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.



Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
"""

class Solution:
    def sortString(self, s: str) -> str:
        qtd_table = {}
        ordered_uniq_chars = sorted(list(set(s)))
        result = []

        for char in s:
            if qtd_table.get(char) is None:
                qtd_table[char] = 1
            else:
                qtd_table[char] += 1



        while sum(qtd_table.values()) > 0:
            for char in ordered_uniq_chars:
                if qtd_table[char] > 0:
                    result.append(char)
                    qtd_table[char] -= 1

            for i in range(len(ordered_uniq_chars) - 1, -1, -1):
                char = ordered_uniq_chars[i]

                if qtd_table[char] > 0:
                    result.append(char)
                    qtd_table[char] -= 1


        return ''.join(result)


import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(Solution().sortString(s="aaaabbbbcccc"), 'abccbaabccba')

if __name__ == '__main__':
    unittest.main()
