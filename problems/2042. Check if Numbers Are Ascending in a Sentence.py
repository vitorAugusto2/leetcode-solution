class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = 0

        for token in s.split():
            if token.isdigit():
                current = int(token)
                if current <= prev:
                    return False
                prev = current

        return True
