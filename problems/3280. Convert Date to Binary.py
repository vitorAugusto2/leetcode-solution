class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year_month_day = date.split("-")
        dates = []
        
        for i in year_month_day:
            dates.append(bin(int(i))[2:])

        return f"{dates[0]}-{dates[1]}-{dates[2]}"
    
    
"""
Another Approach
----------------

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(bin(int(i))[2:] for i in date.split("-"))
        
* Time complexity: 
"""