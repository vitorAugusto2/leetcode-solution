class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        remainder = len(s) % k
        
        if remainder != 0:
            s += fill * (k - remainder)
        
        return [s[i:i + k] for i in range(0, len(s), k)]
