class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        qtd = len(words)
        broken = set(brokenLetters)

        for word in words:
            if len(broken.intersection(word)) >  0:
                qtd -= 1

        return qtd


import unittest
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(Solution().canBeTypedWords(text="leet code", brokenLetters="lt"), 1)


if __name__ == "__main__":
    unittest.main()



