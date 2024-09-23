class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        
        for i in range(len(accounts)):
            wealth.append(sum(accounts[i]))
                
        return max(wealth)
    
"""
Another Approach
----------------

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for account in accounts:
            max_wealth = max(max_wealth, sum(account))
                
        return max_wealth

* Time complexity: O(n)
"""