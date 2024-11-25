class Solution:
    def maxScore(self, s: str) -> int:
        sum_zero = 0
        sum_one = s.count("1")
        max_score = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                sum_zero += 1
            else:
                sum_one -= 1

            max_score = max(max_score, sum_zero + sum_one)

        return max_score
