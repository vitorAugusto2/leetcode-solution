class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        ans = 0
        
        for word in count1:
            if count1[word] == 1 and count2[word] == 1:
                ans += 1
        
        return ans

"""
Another Approach
----------------

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        return sum(1 for word in count1 if count1[word] == 1 and count2[word] == 1)
        
* Time Complexity | Space: O(n + m) | O(n + m)
""" 