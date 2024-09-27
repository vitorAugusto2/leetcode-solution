class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        small_nums = [] 
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    count += 1
            small_nums.append(count)
                
        return small_nums
    
"""
Another Approach
----------------

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101 
        
        for num in nums:
            count[num] += 1
        
        smaller_count = [0] * 101
        
        for i in range(1, 101):
            smaller_count[i] = smaller_count[i - 1] + count[i - 1]
        
        return [smaller_count[num] for num in nums]

    
* Time complexity: O(n) | O(1)
"""