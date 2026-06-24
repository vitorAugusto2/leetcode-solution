class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]

# Complexity (time:space): O(n) | O(n)

"""
Another Solution
----------------

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * (2*n)

        for i in range(n):
            ans[i] = nums[i]
            ans[2*n - 1 - i] = nums[i]

        return ans

# Complexity (time:space): O(n) | O(n)
"""
