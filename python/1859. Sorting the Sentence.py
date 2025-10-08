"""
Approach
--------

1. Split the string into words
2. Create a list of empty positions for words
3. Arrange the words in their correct positions
    3.1. Accesses the last character of the word, which is the index of the word in the sentence
    3.2. Remove the last character
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        words_disord = s.split(" ")
        words_ord = [None] * len(words_disord)
        
        for word in words_disord:
            words_ord[int(word[-1])-1] = word[:-1]

        return " ".join(words_ord)