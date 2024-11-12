class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lr = s.lower().replace(" ", "")
        s_new = ""

        for char in s_lr:
            if char.isalnum():
                s_new += char

        return s_new == s_new[::-1]


"""
Another Approach
================

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = " ".join(char.lower() for char in s if char.isalnum())
        return s == s[::-1]


* Time Complexity:
"""