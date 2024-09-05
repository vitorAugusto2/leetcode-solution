class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        count = 0
        
        for char in s:
            if char == "(":
                count += 1
                max_depth = max(max_depth, count)
            elif char == ")":
                count -= 1

        return max_depth