# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        arr = []
        for i in range(len(sentences)):
            arr.append(sentences[i].count(" ") + 1)
    
        return max(arr)
```