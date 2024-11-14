class Solution:
    def firstUniqChar(self, s: str) -> int:
        hs = Counter(s)

        for idx, value in enumerate(s):
            if hs[value] == 1:
                return idx
        return -1
