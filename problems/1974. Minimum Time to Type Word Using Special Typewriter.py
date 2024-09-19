class Solution:
    def minTimeToType(self, word: str) -> int:
        sec = 0
        current_char = "a"
        
        for char in word:
            diff = abs(ord(char) - ord(current_char))
            move = min(diff, 26 - diff)
            sec += move + 1  
            current_char = char
        
        return sec