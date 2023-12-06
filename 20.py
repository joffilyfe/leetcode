"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        stack = []

        # opening = ['[', '(', '{']
        # closing = [']', ')', '}']

        # for bracket in s:
        #     if bracket in opening:
        #         stack.append(bracket)
        #     else:
        #         if len(stack) == 0:
        #             return False

        #         last = stack.pop()

        #         if last not in opening:
        #             return False

        # return len(stack) == 0

        opening = ['[', '(', '{']
        # closing = [']', ')', '}']
        pairs = ['[]', '()', '{}']

        for bracket in s:
          if bracket in opening:
            stack.append(bracket)
            continue

          # impossible to pop
          if len(stack) == 0:
            return False

          first_out = stack.pop()
          if f"{first_out + bracket}" not in pairs:
            return False

        return len(stack) == 0




print(Solution().isValid(s='['))
