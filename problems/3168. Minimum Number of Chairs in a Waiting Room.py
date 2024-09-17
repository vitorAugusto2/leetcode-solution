class Solution:
    def minimumChairs(self, s: str) -> int:
        max_chairs = 0  
        chairs = 0 
         
        for char in s:
            if char == "E":  
                chairs += 1
                if chairs > max_chairs:
                    max_chairs = chairs 
            else:  
                chairs -= 1
        
        return max_chairs
    
# O(n) | O(1)