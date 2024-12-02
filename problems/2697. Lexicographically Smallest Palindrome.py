class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        chars = list(s)
        left = 0
        right = len(chars) - 1

        while left < right:
            if chars[left] != chars[right]:
                smaller_char = min(chars[left], chars[right])
                chars[left] = chars[right] = smaller_char

            left += 1
            right -= 1

        return "".join(chars)