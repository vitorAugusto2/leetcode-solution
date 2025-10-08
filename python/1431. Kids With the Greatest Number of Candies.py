class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        
        for candie in candies:
            if max(candies) <= candie + extraCandies:
                res.append(True)
            else:
                res.append(False)
        
        return res


"""
Another Approach
----------------

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candie = max(candies)

        return [(candie + extraCandies) >= max_candie for candie in candies]
        
* Time complexity: O(n)    
"""
        