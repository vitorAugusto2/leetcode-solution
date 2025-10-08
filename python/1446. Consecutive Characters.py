class Solution:
    def maxPower(self, s: str) -> int:
        value = 1
        power = 1

        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                value += 1
                power = max(value, power)
            else:
                value = 1

        return power