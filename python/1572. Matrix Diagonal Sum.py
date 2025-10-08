class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_total = 0
        n = len(mat)
        
        for i in range(n):
            sum_total += mat[i][i]
            if i != n - i - 1:
                sum_total += mat[i][n - i - 1]
                
        return sum_total 