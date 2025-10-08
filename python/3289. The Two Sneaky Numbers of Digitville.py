class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = Counter(nums) 
        sneaky_nums = [] 
        
        for key, value in freq.items(): 
            if value > 1:
                sneaky_nums.append(key) 
                
        return sneaky_nums