class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        ans = []
        
        for char in s:
            if char == "I":
                ans.append(low)
                low += 1
            elif char == "D":  
                ans.append(high)
                high -= 1
        
        ans.append(low)  
        return ans
