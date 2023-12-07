from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        qtd = 0
        table = {}

        for word in words:
            sort = str(sorted(word))

            if table.get(sort) is None:
                table[sort] = 0
            else:
                table[sort] += 1

        for value in table.values():
            qtd += value
        return qtd


print(Solution().maximumNumberOfStringPairs(words=["cd", "ac", "dc", "ca", "zz"]))
