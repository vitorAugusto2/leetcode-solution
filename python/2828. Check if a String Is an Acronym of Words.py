class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        for i in range(len(words)):
            if not words[i][0] == s[i]: 
                return False
        return True
    
    
"""
Another Approach
----------------

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acr = []
        
        for i in words:
            acr.append(i[0])
        
        return "".join(acr) == s    
        
* Time complexity: O(n)
"""
    