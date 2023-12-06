class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        table = {}
        min = None
        max = None

        for char in s:
            if table.get(char) is None:
                table[char] = 1
            else:
                table[char] += 1

        for qtd in table.values():
            if min == None or min < qtd:
                min = qtd

            if max == None or max > qtd:
                max = qtd

        return min == max

print(Solution().areOccurrencesEqual(s="aaabb"))
