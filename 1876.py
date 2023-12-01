class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        size = len(s)
        i = 0
        good_string_qtd = 0

        # while i < size - 1:
        #     if i+2 > size-1:
        #         break

        #     if len(set(s[i:i+3])) == 3:
        #         good_string_qtd += 1

        #     i += 1

        for i in range(size - 1):
            if i + 2 > size - 1:
                break

            if len(set(s[i : i + 3])) == 3:
                good_string_qtd += 1

        return good_string_qtd


import unittest


class Tests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(Solution().countGoodSubstrings(s="aababcabc"), 4)


unittest.main()
