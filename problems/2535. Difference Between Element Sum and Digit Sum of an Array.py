class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums) 
        digit_sum = 0
        
        for i in nums:
            for j in str(i):
                digit_sum += int(j)
        
        return abs(element_sum - digit_sum)