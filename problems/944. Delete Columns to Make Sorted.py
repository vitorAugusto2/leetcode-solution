class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        ans = 0
            
        for i in range(n):
            for j in range(1, m):
                if strs[j][i] < strs[j-1][i]:
                    ans += 1
                    break
            
        return ans
