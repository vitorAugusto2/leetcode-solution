class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums) 
        
        for idx, num in enumerate(nums):
            left += num
            nums[idx] = abs(right - left)
            right -= num

        return nums