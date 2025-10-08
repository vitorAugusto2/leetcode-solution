class Solution: 
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        text_space = text.split(" ")
        
        for word in text_space:
            if all(letter not in word for letter in brokenLetters):
                ans += 1
                          
        return ans