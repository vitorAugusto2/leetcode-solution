class Solution:
    def greatestLetter(self, s: str) -> str:
        chars = set(s)
            
        for char in range(ord("Z"), ord("A") - 1, -1):
            u = chr(char)
            l = chr(char + 32)
            if u in chars and l in chars:
                return u

        return ""

    print(greatestLetter(None, "lEeTcOdE"))