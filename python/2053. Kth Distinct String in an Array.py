class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        distinct_str  = []

        for key, value in count.items():
            if value == 1:
                distinct_str.append(key)

        return distinct_str[k-1] if len(distinct_str) >= k else ""


"""
Another Approach
================

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        
        for i in arr:
            if count[i] == 1:  
                k -= 1
                if k == 0:  
                    return i
        
        return ""

* Time Complexity: O(n)
* Space Complexity: O(n)
"""