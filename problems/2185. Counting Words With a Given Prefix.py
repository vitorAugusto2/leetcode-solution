class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        
        for word in words:
            if word[:len(pref)] == pref:
                count += 1
                
        return count
    

"""
Another Approach
----------------

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        
        for word in words:
            if word.startswith(pref):
                count += 1
                
        return count
        
* Time complexity: O(n)
"""