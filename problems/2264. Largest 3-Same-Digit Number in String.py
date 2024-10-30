class Solution:
    def largestGoodInteger(self, num: str) -> str:
        dict_nums_triplet = {
            0 : "999",
            1 : "888",
            2 : "777",
            3 : "666",
            4 : "555",
            5 : "444",
            6 : "333",
            7 : "222",
            8 : "111",
            9 : "000",
            10 : ""
        }
        
        for triplet in dict_nums_triplet.values():
            if triplet in num:
                return triplet

"""
Another Approach
----------------

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for digit in "9876543210":
            triplet = digit * 3
            
            if triplet in num:
                return triplet
                
        return ""
        
* Time Complexity: O(n) | O(1)
""" 
