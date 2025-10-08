class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict_freq = {}
        
        for char in s:
            dict_freq[char] = dict_freq.get(char, 0) + 1
            
        values = list(dict_freq.values())
        
        return all(value == values[0] for value in values)
    
"""
Another Approach
----------------

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
        
* Time complexity: O(n)
"""