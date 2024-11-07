class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            ans = ""
            groups = [s[i:i + k] for i in range(0, len(s), k)]

            for group in groups:
                group_sum = sum(int(char) for char in group)
                ans += str(group_sum)

            s = ans

        return s