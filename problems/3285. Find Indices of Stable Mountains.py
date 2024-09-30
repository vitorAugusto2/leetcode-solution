class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []
        
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                ans.append(i)
        
        return ans  
     
    
"""
Another Approach
----------------

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1, len(height)) if height[i-1] > threshold]


* Time Complexity: O(n)

---

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i, h in enumerate(height[1:], start=1) if height[i - 1] > threshold]
        
* Time Complexity: O(n)
"""