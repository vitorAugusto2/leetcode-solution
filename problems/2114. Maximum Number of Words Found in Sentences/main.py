class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        arr = []
        for i in range(len(sentences)):
            arr.append(sentences[i].count(" ") + 1)
    
        return max(arr)
    

"""
Another Approach
----------------

class Solution:
    return max(i.count(" ") for i in sentences) + 1
        
* Time complexity: O(n)
"""