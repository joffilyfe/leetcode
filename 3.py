import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        max_length = 0
        hashset = set()

        for right in range(n):
            char = s[right]

            while char in hashset:
                leftmost_char = s[left]
                hashset.remove(leftmost_char)
                left += 1

            hashset.add(char)

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
