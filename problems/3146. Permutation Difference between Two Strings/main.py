class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        perm_diff = 0

        for i in range(len(s)):
            perm_diff += abs(s.index(s[i]) - t.index(s[i]))
            
        return perm_diff
    
"""
Another Approach
----------------

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos_s = {char: i for i, char in enumerate(s)}   
        pos_t = {char: i for i, char in enumerate(t)}   
        
        perm_diff = 0

        for char in s:
            perm_diff += abs(pos_s[char] - pos_t[char])
        
        return perm_diff
        
* Time complexity: O(n)
"""