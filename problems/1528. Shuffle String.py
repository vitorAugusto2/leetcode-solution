class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return "".join([t for _, t in sorted(zip(indices, s))])