"""
Approach
--------

1. Iterate over the first half of the string.
2. For each character in the first half, check if it is a vowel and increment the count for the first half.
3. Simultaneously, check characters from the end of the string moving towards the middle for the second half and 
increment the count for the second half.
4. Compare the counts of vowels in both halves.
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = set("aeiouAEIOU") 
        n = len(s)
        count1 = 0
        count2 = 0

        for i in range(n // 2):
            if s[i] in vowel:
                count1 += 1
            if s[n-1-i] in vowel:
                count2 += 1

        return count1 == count2