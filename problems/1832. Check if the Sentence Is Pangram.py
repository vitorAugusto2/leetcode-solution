class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        char = []
        
        for c in sentence:
            if not c in char:
                char.append(c)
        
        return len(char) == 26        