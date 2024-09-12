class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_merge = []
        p1 = 0
        p2 = 0
        
        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                word_merge.append(word1[p1])
                p1 += 1
            if p2 < len(word2):
                word_merge.append(word2[p2])
                p2 += 1

        return "".join(word_merge)
    
"""
Another Approach
----------------

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Utiliza zip_longest para combinar as duas palavras
        word_merge = [char1 + char2 for char1, char2 in zip_longest(word1, word2, fillvalue="")]
        return "".join(word_merge)
        
* Time complexity: O(n + m)
"""