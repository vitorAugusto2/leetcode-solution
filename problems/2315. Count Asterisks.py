"""
Approach
----------------

1. bool 'toggle' to toggle 
2. Loop through each character of the string 's'
3. Check whether counting asterisks is allowed or not
"""

class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0 
        toggle = True
        
        for char in s:
            if char == "|":
                toggle = not toggle
            elif toggle and char == "*":
                count += 1
        
        return count