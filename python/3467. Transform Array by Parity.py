from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if num % 2 == 0:
                ans.append(0)
            else:
                ans.append(1)

        return sorted(ans)

# Time Complexity (time|space): O(n log n) | O(n)


"""
Another Approach
----------------

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even_num = 0

        for num in nums:
            if num % 2 == 0:
                even_num += 1

        return [0] * even_num + [1] * (len(nums) - even_num)

# Time Complexity (time|space): O(n) | O(n)
"""
