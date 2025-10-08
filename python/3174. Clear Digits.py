class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []

        for char in s:
            if char.isalpha():
                ans.append(char)
            elif ans:
                ans.pop()

        return "".join(ans)