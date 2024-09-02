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
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for idx, value in enumerate(words):
            if x in value:
                result.append(idx)
        
        return result
```