class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        count_num = Counter(nums)

        for key, value in count_num.items():
            if value == 2:
                ans.append(key)

        return ans

# Time Complexity (time|space): O(n) | O(n)
