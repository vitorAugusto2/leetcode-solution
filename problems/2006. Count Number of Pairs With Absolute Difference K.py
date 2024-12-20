from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0 
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i < j and abs(nums[i] - nums[j]) == k:
                    count += 1
        
        return count
    
    print(countKDifference(None, [1,2,2,1], 1))