class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    ans += 1

        return ans

# Time Complexity (time|space): O(n^2) | O(1)

"""
Another Approach
----------------

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        ans = 0

        for n in frequency.values():
            ans += n * (n - 1) // 2

        return ans

# Time Complexity (time|space): O(n) | O(n)
"""
