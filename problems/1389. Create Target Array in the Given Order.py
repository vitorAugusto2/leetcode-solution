class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        
        for num, idx in zip(nums, index):
            ans.insert(idx, num)
            
        return ans
    

"""
Another Approach
----------------

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [0] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i, index[i], -1):
                target[j] = target[j - 1]
            target[index[i]] = nums[i]
        
        return target

* Time Complexity: O(n^2) | O(n)
"""