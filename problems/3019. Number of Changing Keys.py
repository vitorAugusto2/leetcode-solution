class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0 
        s_lower = s.lower()

        for i in range(len(s_lower) - 1):
            if s_lower[i] != s_lower[i + 1]:
                count += 1

        return count 
