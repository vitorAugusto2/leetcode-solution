class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_sum = sum(nums)
        left_sum = 0
        ans = []

        for num in nums:
            right_sum -= num
            ans.append(abs(left_sum - right_sum))
            left_sum += num


        return ans

# Time Complexity (time|space): O(n) | O(n)
