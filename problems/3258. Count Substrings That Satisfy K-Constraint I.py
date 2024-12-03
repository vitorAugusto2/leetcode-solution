class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        i = 0
        count_ones = 0

        for j in range(len(s)):
            if s[j] == "1":
                count_ones += 1

            while count_ones > k and (j - i + 1 - count_ones) > k:
                if s[i] == "1":
                    count_ones -= 1
                i += 1

            ans += j - i + 1

        return ans