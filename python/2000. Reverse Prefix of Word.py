"""
Approach
--------

1. Find index of 'ch'
2. Check if 'ch' exists, if False, returns 'word'
3. Reverse the Prefix and concatenate the rest of the 'word'
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx_ch = word.find(ch)
        
        if idx_ch != -1:
            return word[:idx_ch+1][::-1] + word[idx_ch+1:]  
        else:
            return word
        