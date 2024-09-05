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

        for i in s:
            if i == "(":
                if count > 0:
                    result.append(i)
                count += 1
            elif i == ")":
                count -= 1
                if count > 0:
                    result.append(i)

        return "".join(result)