class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        current_value = 0
        
        for s in strs:
            if s.isnumeric():
                current_value = max(current_value, int(s)) 
            else:
                current_value = max(current_value, len(s)) 
        
        return current_value