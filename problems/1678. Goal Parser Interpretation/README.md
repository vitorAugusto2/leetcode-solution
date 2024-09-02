# Title
## Approach
<!-- Describe your approach to solving the problem. -->

## Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code
```python3 
class Solution:
    def interpret(command: str) -> str:
        arr = []
        
        for i in range(len(command)):
            if "G" in command[i]:
                arr.append("G")
            elif "(" in command[i]:
                if ")" in command[i+1]:
                    arr.append("o")
                else:
                    arr.append("al")
                    
        return "".join(arr)

```