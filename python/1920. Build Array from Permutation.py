class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        i = 1

        for i in nums:
            ans[i] = nums[nums[i]]

        return ans

# Time Complexity (time:space): O(n) | O(n)

"""
Another Approach
----------------

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            num_new = nums[nums[i] % n] % n
            nums[i] = nums[i] + n * num_new

        for i in range(n):
            nums[i] = nums[i] // n

        return nums

# Time Complexity (time:space): O(n) | O(1)
"""
