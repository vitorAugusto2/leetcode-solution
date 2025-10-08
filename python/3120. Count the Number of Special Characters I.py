class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = set()

        for char in word:
            if char.islower() and char.upper() in word:
                ans.add(char)

        return len(ans)

"""
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = []

        for char in word:
            if char.islower() and chr(ord(char) - 32) in word and char not in ans:
                ans.append(char)

        return len(ans)
        
# Time Complexity and space: O(n) | O(n)
"""