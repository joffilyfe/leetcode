import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        n = len(s)
        left = 0
        max_length = 0

        for right in range(n):
            char = s[right]
            table[char] = table.get(char, 0) + 1

            while any(count > 1 for count in table.values()):
                leftmost_char = s[left]
                table[leftmost_char] -= 1

                if table[leftmost_char] == 0:
                    del table[leftmost_char]

                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length



class Tests(unittest.TestCase):
    def test_one(self):
        s = "abcabcbb"

        self.assertEqual(Solution().lengthOfLongestSubstring(s), 3)

    def test_two(self):
        s = "bbbbb"

        self.assertEqual(Solution().lengthOfLongestSubstring(s), 1)

    def test_three(self):
        s = "pwwkew"

        self.assertEqual(Solution().lengthOfLongestSubstring(s), 3)

if __name__ == "__main__":
    unittest.main()
