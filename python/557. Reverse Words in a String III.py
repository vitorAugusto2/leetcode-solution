class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words_inv = []
        
        for word in words:
            words_inv.append(word[::-1])
        
        return " ".join(words_inv)