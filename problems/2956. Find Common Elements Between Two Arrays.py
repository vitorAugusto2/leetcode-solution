class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        left = 0
        right = 0

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                left += 1
        
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                right += 1
        
        return [left, right]
    
"""
Another Approach
----------------

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        
        left = sum(1 for num in nums1 if num in set_nums2)
        right = sum(1 for num in nums2 if num in set_nums1)
        
        return [left, right]

* Time Complexity: O(n + m)
"""