class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_sorted = sorted([point for point, _ in points])

        max_width = 0
        
        for i in range(len(x_sorted) - 1):
            max_width = max(max_width, x_sorted[i+1] - x_sorted[i])
            
        return max_width