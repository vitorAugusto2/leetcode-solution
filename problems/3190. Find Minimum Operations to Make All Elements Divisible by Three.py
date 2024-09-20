class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op = 0
        
        for num in range(len(nums)):
            if nums[num] % 3 != 0:
                if nums[num] % 3 == 1:
                    nums[num] -= 1
                    op += 1
                if nums[num] % 3 == 2:
                    nums[num] += 1
                    op += 1
        return op
    
"""
Another Approach
----------------

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op = 0
        
        for i in range(len(nums)):
            mod = nums[i] % 3
            if mod != 0:
                nums[i] += (1 if mod == 2 else -1)
                op += 1
                
        return op
        
* Time complexity: O(n)
"""