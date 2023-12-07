# https://leetcode.com/problems/minimize-string-length/


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        table = {}

        for char in s:
            if table.get(char) is None:
                table[char] = 1
            else:
                table[char] += 1

        return len(table)


import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(Solution().minimizedStringLength(s="aaabc"), 3)
        self.assertEqual(Solution().minimizedStringLength(s="cbbd"), 3)
        self.assertEqual(Solution().minimizedStringLength(s="dddaaa"), 2)


if __name__ == "__main__":
    unittest.main()
