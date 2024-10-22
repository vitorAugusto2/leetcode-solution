class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i] == "b" and s[i + 1] == "a":
                return False
        return True
    
"""
Another Approach
----------------

class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s
        
# Time Complexity: O(n) | O(1)
"""