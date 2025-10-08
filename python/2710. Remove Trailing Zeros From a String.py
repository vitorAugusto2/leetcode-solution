class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip("0")
        

"""
Another approach
----------------

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num_list = list(num)

        while num_list[-1] == "0":
            num_list.pop()    

        return "".join(num_list)

* O(n)
"""

