class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0 
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        
        return count
     
    
"""
Another Approach
----------------

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = 0
        
        for v in freq.values():
            count += (v * (v - 1)) // 2  

        return count

* Time complexity: O(n)
"""

