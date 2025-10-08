"""
Approach
--------

1. Init
    * 'count' -> depth level 
    * 'result' -> stores parameters that are not external
2. Iterate over each character of 's'
    * if 'count' equals 0, 's' is an outer parentheses
    * if 'count' is different from 0, 's' is an internal parenthesis
3. .join result to join into a string
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        result = []

        for char in s:
            if char == "(":
                if count > 0:
                    result.append(char)
                count += 1
            elif char == ")":
                count -= 1
                if count > 0:
                    result.append(char)

        return "".join(result)
