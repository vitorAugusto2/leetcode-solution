class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0

        for idx, num in enumerate(nums):
            if idx % 2 == 0:
                ans += num
            else:
                ans -= num
        
        return ans

# Time Complexity (time|space): O(n) | O(1)
