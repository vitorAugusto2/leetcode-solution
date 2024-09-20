class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:] * 2
        return ans
    
"""
Another Approach
----------------

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
        
* Time complexity: O(n)
"""
    