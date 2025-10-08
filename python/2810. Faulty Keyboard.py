class Solution:
    def finalString(self, s: str) -> str:
        new_s = []
        
        for char in s:
            if char != "i":
                new_s.append(char)
            else:
                new_s.reverse()
            
        return "".join(new_s)
    
"""
Another Approach
----------------

class Solution:
    def finalString(self, s: str) -> str:
        result = []
        reverse_mode = False
        
        for char in s:
            if char == "i":
                reverse_mode = not reverse_mode
            else:
                if reverse_mode:
                    result.insert(0, char)  # Adiciona no início da lista
                else:
                    result.append(char)     # Adiciona no final da lista
        
        return "".join(result)

* Time complexity: O(n)
        
"""