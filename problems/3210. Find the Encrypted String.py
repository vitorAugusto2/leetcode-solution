class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)

        for i in range(n):
            j = (i + k) % n
            ans += s[j]
            
        return ans