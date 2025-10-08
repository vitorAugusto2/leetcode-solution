class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        qte = 0
        
        for i in range(len(items)):
            if ruleKey == "type" and ruleValue == items[i][0]:
                qte += 1
            elif ruleKey == "color" and ruleValue == items[i][1]:
                qte += 1
            elif ruleKey == "name" and ruleValue == items[i][2]:
                qte += 1
                
        return qte

"""
Another Approach
----------------

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {"type": 0, "color": 1, "name": 2}
        return sum(1 for item in items if item[d[ruleKey]] == ruleValue)
        
* Time complexity: O(n)
"""