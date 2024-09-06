"""
Approach
----------------

1. 'allowed' is converted to a set
2. Correct each word in the list
3. Check whether the word set is a subset of the allowed set
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_allowed = set(allowed)  
        count = 0

        for word in words:
            if set(word) <= set_allowed:
                count += 1
                
        return count