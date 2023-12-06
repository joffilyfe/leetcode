"""
 pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false

"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = {}

        for char in sentence:
            if alphabet.get(char) is None:
                alphabet[char] = 1
            else:
                alphabet[char] += 1

        return len(alphabet) == 26

print(Solution().checkIfPangram(sentence='thequickbrownfoxjumpsoverthelazydog'))
