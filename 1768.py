import unittest

# https://leetcode.com/problems/merge-strings-alternately/


class Solution:
    """The intuition behind this problem is simple:
    1) Use two pointers to track what is the current letter from each strings
    2) Loop while each pointer is less than its pointer size
    3) Append the string with letters in the order: word1 then word2
    4) Return the result string
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1Size = len(word1)
        word2Size = len(word2)
        word1Pointer = 0
        word2Pointer = 0

        res = ""

        while word1Pointer < word1Size or word2Pointer < word2Size:
            if word1Pointer < word1Size:
                res += word1[word1Pointer]
                word1Pointer += 1

            if word2Pointer < word2Size:
                res += word2[word2Pointer]
                word2Pointer += 1

        return res


class Tests(unittest.TestCase):
    def test_one(self):
        word1 = "abc"
        word2 = "pqr"

        self.assertEqual(Solution().mergeAlternately(word1, word2), "apbqcr")

    def test_two(self):
        word1 = "ab"
        word2 = "pqrs"

        self.assertEqual(Solution().mergeAlternately(word1, word2), "apbqrs")


if __name__ == "__main__":
    unittest.main()
