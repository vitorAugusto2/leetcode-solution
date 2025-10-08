class Solution:
    def countSegments(self, s: str) -> int:
        s.replace("!@#$%^&*()_+-=',.:", " ")

        return len(s.split())