class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        table = {}
        alphabet_position = 0
        result = []
        key = key

        for i in range(len(key)):
            if key[i] == " ":
                continue

            if table.get(key[i]) is not None:
                continue

            table[key[i]] = chr(alphabet_position + 97)
            alphabet_position += 1

        for chunk in message.split(" "):
            word = ""

            for char in chunk:
                if char == " ":
                    word += " "
                    continue
                else:
                    word += table.get(char)

            result.append(word)

        return " ".join(result)


print(
    Solution().decodeMessage(
        key="the quick brown fox jumps over the lazy dog", message="vkbs bs t suepuv"
    )
)
