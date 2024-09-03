class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        aux = 0
    
        for i in range(len(s)): 
            if s[i] == "R":     
                aux += 1        
            else:
                aux -= 1
            if aux == 0:        
                count += 1

        return count