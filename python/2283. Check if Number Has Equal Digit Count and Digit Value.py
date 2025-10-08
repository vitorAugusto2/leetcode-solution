class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if int(num[i]) != num.count(str(i)):
                return False
        return True
    
    
"""
Another Approach
----------------

class Solution:
    def digitCount(self, num: str) -> bool:
        digit_count = [0] * 10 
        
        for digit in num:
            digit_count[int(digit)] += 1
        
        for i in range(len(num)):
            if int(num[i]) != digit_count[i]:
                return False
        
        return True

* Time Complexity: O(n) | O(1)

"""