class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        
        for i in range(n):                     
            for j in range(1, n - i + 1, 2):
                ans += sum(arr[i:i + j])

        return ans