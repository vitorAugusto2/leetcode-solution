class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        count = 0
        
        for num in nums:
            if num < k:
                count += 1
        
        return count


"""
Another Approach
----------------

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(1 for num in nums if num < k)

* Time Complexity: O(n)
"""