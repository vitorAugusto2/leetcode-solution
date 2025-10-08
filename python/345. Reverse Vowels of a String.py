class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        char_s = list(s)
        left = 0
        right = len(char_s) - 1

        while left < right:
            if char_s[left] not in vowels:
                left += 1
            elif char_s[right] not in vowels:
                right -= 1
            else:
                char_s[left], char_s[right] = char_s[right], char_s[left]
                left += 1
                right -= 1

        return "". join(char_s)