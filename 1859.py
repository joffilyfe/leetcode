class Solution:
    def sortSentence(self, s: str) -> str:
        words = sorted(s.split(' '), key=lambda x: int(x[-1]))

        return " ".join(map(lambda x: x[0:-1], words))
