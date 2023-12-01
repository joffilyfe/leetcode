class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        qtd = len(words)
        broken = set(brokenLetters)

        for word in words:
            if len(broken.intersection(word) > 0):
                qtd -= 1

        return qtd


print(Solution().canBeTypedWords(text="leet code", brokenLetters="lt"))
