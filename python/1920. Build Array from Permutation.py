class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        
        return ans
    
"""
Another Approach
----------------

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
        
* Time complexity: O(n)
"""
    