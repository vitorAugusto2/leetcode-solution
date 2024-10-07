class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uncommon_words = []
        
        s1_words = s1.split()
        s2_words = s2.split()

        all_words = s1_words + s2_words
        
        words_count = Counter(all_words)
        
        for word in words_count:
            if words_count[word] == 1:
                uncommon_words.append(word)

        return uncommon_words
    
"""
Another Approach
----------------

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words_count = Counter(s1.split() + s2.split())
        
        return [word for word, count in words_count.items() if count == 1]

* Time complexity: O(n+m) | O(n+m+k)
"""